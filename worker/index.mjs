// Sites supplies trusted identity headers and the D1/ASSETS bindings.
const ORIGIN = 'https://geniva-web.ozkanozdemir.chatgpt.site';
const NOTICE_VERSION = '2026-11-16';
const CONSENT = __CONSENT_TEXT__;
const INBOX_PAGE = __INBOX_HTML__;
const TOPICS = new Set(['general','demo','software','hardware','training','career']);
const json = (data,status=200) => new Response(JSON.stringify(data), {status,headers:{'Content-Type':'application/json; charset=utf-8','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}});
const isSameOrigin = request => [ORIGIN,new URL(request.url).origin].includes(request.headers.get('Origin'));
const isOwner = (request,env) => Boolean(env.INBOX_OWNER_EMAIL && request.headers.get('oai-authenticated-user-id') && request.headers.get('oai-authenticated-user-email')?.toLowerCase() === env.INBOX_OWNER_EMAIL.toLowerCase());
const clean = (value,max) => typeof value === 'string' && value.trim().length <= max ? value.trim() : null;

async function readBody(request) {
 if (!request.headers.get('Content-Type')?.startsWith('application/json')) throw new Error('format');
 const reader = request.body?.getReader();
 if (!reader) throw new Error('body');
 const chunks=[];let size=0;
 while(true){const {done,value}=await reader.read();if(done)break;size+=value.length;if(size>20000){await reader.cancel();throw new Error('size');}chunks.push(value);}
 const bytes=new Uint8Array(size);let offset=0;for(const chunk of chunks){bytes.set(chunk,offset);offset+=chunk.length;}
 return JSON.parse(new TextDecoder().decode(bytes));
}

async function contact(request,env) {
 if(request.method!=='POST') return json({error:'method'},405);
 if(!isSameOrigin(request))return json({error:'origin'},403);
 let input;try{input=await readBody(request);}catch{return json({error:'invalid'},400);}
 if(!input || typeof input!=='object' || Array.isArray(input))return json({error:'invalid'},400);
 if(input.website)return json({error:'invalid'},400);
 const data={};
 for(const [key,max] of Object.entries({name:120,email:254,organization:160,phone:40,preferred_time:160,message:4000,portfolio_url:1000})){
  data[key]=clean(input[key]??'',max);
  if(data[key]===null)return json({error:'invalid',field:key},400);
 }
 data.email=data.email.toLowerCase();
 if(!data.name || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email) || data.message.length<10)return json({error:'invalid'},400);
 if(!TOPICS.has(input.topic) || !['en','tr'].includes(input.language) || !['email','phone'].includes(input.reply_by) || typeof input.marketing_opt_in!=='boolean')return json({error:'invalid'},400);
 if(input.reply_by==='phone' && data.phone.replace(/\D/g,'').length<7)return json({error:'phone',field:'phone'},400);
 if(data.portfolio_url){try{if(!['https:','http:'].includes(new URL(data.portfolio_url).protocol))throw new Error();}catch{return json({error:'invalid',field:'portfolio_url'},400);}}
 if(!/^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(input.id??''))return json({error:'invalid'},400);
 if(!env.DB || !env.FORM_RATE_LIMIT_SALT)return json({error:'unavailable'},503);
 try{
  const existing=await env.DB.prepare('SELECT email FROM enquiries WHERE id = ?').bind(input.id).first();
  if(existing)return existing.email===data.email ? json({ok:true,id:input.id}) : json({error:'conflict'},409);
  const now=new Date(),since=new Date(now.getTime()-3600000).toISOString();
  const client=request.headers.get('cf-connecting-ip') || request.headers.get('oai-authenticated-user-id') || data.email;
  const digest=await crypto.subtle.digest('SHA-256',new TextEncoder().encode(env.FORM_RATE_LIMIT_SALT+'|'+now.toISOString().slice(0,10)+'|'+client));
  const rateKey=Array.from(new Uint8Array(digest),b=>b.toString(16).padStart(2,'0')).join('');
  const limit=await env.DB.prepare('SELECT COUNT(*) AS total, COALESCE(SUM(CASE WHEN email = ? THEN 1 ELSE 0 END),0) AS per_email, COALESCE(SUM(CASE WHEN rate_key = ? THEN 1 ELSE 0 END),0) AS per_client FROM enquiries WHERE created_at >= ?').bind(data.email,rateKey,since).first();
  if(limit.total>=200 || limit.per_email>=5 || limit.per_client>=12)return json({error:'rate_limit'},429);
  const created=now.toISOString();
  const result=await env.DB.prepare('INSERT OR IGNORE INTO enquiries (id,created_at,name,email,organization,phone,preferred_time,topic,reply_by,message,portfolio_url,language,marketing_opt_in,marketing_consent_text,marketing_consent_version,marketing_consented_at,privacy_notice_version,rate_key) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)').bind(input.id,created,data.name,data.email,data.organization,data.phone,data.preferred_time,input.topic,input.reply_by,data.message,input.topic==='career'?data.portfolio_url:'',input.language,input.marketing_opt_in?1:0,CONSENT[input.language],NOTICE_VERSION,input.marketing_opt_in?created:null,NOTICE_VERSION,rateKey).run();
  if(result.meta?.changes===0){const row=await env.DB.prepare('SELECT email FROM enquiries WHERE id = ?').bind(input.id).first();if(row?.email!==data.email)return json({error:'conflict'},409);}
  return json({ok:true,id:input.id},201);
 }catch(error){console.error('Contact storage failed',error?.name || 'Error');return json({error:'unavailable'},503);}
}

async function inbox(request,env) {
 if(!isOwner(request,env))return json({error:'unauthorized'},403);
 if(!env.DB)return json({error:'unavailable'},503);
 try{
  if(request.method==='GET'){
   const offset=Number(new URL(request.url).searchParams.get('offset')||0);
   if(!Number.isInteger(offset)||offset<0||offset>10000)return json({error:'invalid'},400);
   const rows=await env.DB.prepare('SELECT id,created_at,name,email,organization,phone,preferred_time,topic,reply_by,message,portfolio_url,language,marketing_opt_in,marketing_consented_at,reviewed_at FROM enquiries ORDER BY created_at DESC LIMIT 40 OFFSET ?').bind(offset).all();
   const count=await env.DB.prepare('SELECT COUNT(*) AS total FROM enquiries').first();
   return json({items:rows.results,total:count.total,next:offset+rows.results.length<count.total?offset+40:null});
  }
  if(request.method==='PATCH'){
   if(!isSameOrigin(request))return json({error:'origin'},403);
   let data;try{data=await readBody(request);}catch{return json({error:'invalid'},400);}
   if(typeof data?.id!=='string'||data.id.length>40)return json({error:'invalid'},400);
   const result=await env.DB.prepare('UPDATE enquiries SET reviewed_at = ? WHERE id = ?').bind(new Date().toISOString(),data.id).run();
   return result.meta.changes ? json({ok:true}) : json({error:'not_found'},404);
  }
  return json({error:'method'},405);
 }catch{return json({error:'unavailable'},503);}
}

export default {
 async fetch(request,env) {
  const path=new URL(request.url).pathname;
  if(path==='/api/contact')return contact(request,env);
  if(path==='/api/inbox')return inbox(request,env);
  if(path==='/inbox' || path==='/inbox/'){
   if(!request.headers.get('oai-authenticated-user-id'))return new Response('<!doctype html><html lang="en"><meta charset="utf-8"><title>Geniva inbox</title><p><a href="/signin-with-chatgpt?return_to=%2Finbox" target="_top">Sign in to open the Geniva inbox</a></p></html>',{headers:{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store'}});
   if(!isOwner(request,env))return new Response('Access denied',{status:403,headers:{'Cache-Control':'no-store'}});
   return new Response(INBOX_PAGE,{headers:{'Content-Type':'text/html; charset=utf-8','Cache-Control':'private, no-store','X-Content-Type-Options':'nosniff'}});
  }
  if(path.startsWith('/api/'))return json({error:'not_found'},404);
  if(path.endsWith('/')){const url=new URL(request.url);url.pathname+='index.html';return env.ASSETS.fetch(new Request(url,request));}
  return env.ASSETS.fetch(request);
 }
};
