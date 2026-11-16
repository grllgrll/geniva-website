// Exercises the production Worker against SQLite with the D1 API shape.
import assert from 'node:assert/strict';
import {readFileSync,readdirSync} from 'node:fs';
import {DatabaseSync} from 'node:sqlite';
const source=readFileSync(new URL('./dist/server/index.js',import.meta.url),'utf8');
const worker=(await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'))).default;
const db=new DatabaseSync(':memory:');
for(const filename of readdirSync(new URL('./drizzle/',import.meta.url)).filter(name=>name.endsWith('.sql'))) db.exec(readFileSync(new URL('./drizzle/'+filename,import.meta.url),'utf8'));
const DB={prepare(sql){const statement=db.prepare(sql);return {bind(...args){return {async first(){return statement.get(...args)??null;},async all(){return {results:statement.all(...args)};},async run(){return {meta:statement.run(...args)};}};},async first(){return statement.get()??null;}};}};
const origin='https://geniva-web.ozkanozdemir.chatgpt.site';
const env={DB,FORM_RATE_LIMIT_SALT:'test-only',INBOX_OWNER_EMAIL:'owner@example.test',ASSETS:{fetch:async()=>new Response('asset')}};
const base=()=>({id:crypto.randomUUID(),name:'QA Example',email:'qa@example.test',organization:'QA',phone:'',preferred_time:'',topic:'general',reply_by:'email',message:'This is a local test message.',portfolio_url:'',language:'en',marketing_opt_in:false,website:''});
function request(data,headers={}){return new Request(origin+'/api/contact',{method:'POST',headers:{'Content-Type':'application/json',Origin:origin,...headers},body:JSON.stringify(data)});}
const valid=base();let response=await worker.fetch(request(valid),env);assert.equal(response.status,201);
let row=db.prepare('SELECT * FROM enquiries WHERE id=?').get(valid.id);assert.equal(row.marketing_opt_in,0);assert.equal(row.marketing_consented_at,null);assert.match(row.marketing_consent_text,/marketing emails/);
response=await worker.fetch(request(valid),env);assert.equal(response.status,200);assert.equal(db.prepare('SELECT COUNT(*) AS n FROM enquiries WHERE id=?').get(valid.id).n,1);
const concurrent={...base(),email:'concurrent@example.test'};await Promise.all([worker.fetch(request(concurrent),env),worker.fetch(request(concurrent),env)]);assert.equal(db.prepare('SELECT COUNT(*) AS n FROM enquiries WHERE id=?').get(concurrent.id).n,1);
const consent={...base(),language:'tr',email:'consent@example.test',marketing_opt_in:true,topic:'demo',reply_by:'phone',phone:'+90 216 250 4471'};response=await worker.fetch(request(consent),env);assert.equal(response.status,201);row=db.prepare('SELECT * FROM enquiries WHERE id=?').get(consent.id);assert.equal(row.marketing_opt_in,1);assert(row.marketing_consented_at);assert.match(row.marketing_consent_text,/pazarlama/);assert.equal(row.topic,'demo');
for(const values of [{name:''},{email:'bad'},{reply_by:'phone',phone:''},{topic:'unknown'},{marketing_opt_in:'yes'},{portfolio_url:'javascript:alert(1)'},{website:'spam'},{message:'x'},{id:'bad'},{message:'x'.repeat(25000)}]) {response=await worker.fetch(request({...base(),...values}),env);assert.equal(response.status,400,JSON.stringify(values).slice(0,100));}
assert.equal((await worker.fetch(request(base(),{Origin:'https://attacker.example'}),env)).status,403);
assert.equal((await worker.fetch(request(base()),{...env,DB:null})).status,503);
assert.equal((await worker.fetch(request({...base(),email:'broken@example.test'}),{...env,DB:{prepare(){throw new Error('offline');}}})).status,503);
const career={...base(),email:'career@example.test',topic:'career',portfolio_url:'https://example.test/cv'};assert.equal((await worker.fetch(request(career),env)).status,201);
for(let i=0;i<5;i++)assert.equal((await worker.fetch(request({...base(),email:'rate@example.test'}),env)).status,201);
assert.equal((await worker.fetch(request({...base(),email:'rate@example.test'}),env)).status,429);
for(const headers of [{},{'oai-authenticated-user-id':'other','oai-authenticated-user-email':'other@example.test'},{'oai-authenticated-user-email':'owner@example.test'}])assert.equal((await worker.fetch(new Request(origin+'/api/inbox',{headers}),env)).status,403);
const owner={'oai-authenticated-user-id':'owner-site-id','oai-authenticated-user-email':'owner@example.test'};
response=await worker.fetch(new Request(origin+'/api/inbox',{headers:owner}),env);assert.equal(response.status,200);const inbox=await response.json();assert(inbox.items.length>0);assert(!('rate_key' in inbox.items[0]));
assert.equal((await worker.fetch(new Request(origin+'/inbox',{headers:owner}),env)).status,200);
response=await worker.fetch(new Request(origin+'/api/inbox',{method:'PATCH',headers:{...owner,Origin:origin,'Content-Type':'application/json'},body:JSON.stringify({id:valid.id})}),env);assert.equal(response.status,200);assert(db.prepare('SELECT reviewed_at FROM enquiries WHERE id=?').get(valid.id).reviewed_at);
assert.equal(await (await worker.fetch(new Request(origin+'/'),env)).text(),'asset');
assert.equal((await worker.fetch(new Request(origin+'/api/missing'),env)).status,404);
console.log('PASS: Worker storage, consent false/true, TR/EN, demo/career, retry idempotency, validation, throttling, storage failure, private inbox authorization and review state.');
db.close();
