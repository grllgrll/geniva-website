// DOM-level interaction checks. Requires jsdom; no browser rendering is performed.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const { JSDOM } = require(process.env.GENIVA_QA_MODULES ? path.join(process.env.GENIVA_QA_MODULES, 'jsdom') : 'jsdom');
const root = path.join(__dirname, 'dist');
const script = fs.readFileSync(path.join(root, 'app.js'), 'utf8');
const pages = ['index','solutions','software','hardware','training','about','references','contact'];
(async () => {
 for (const language of ['', 'tr/']) {
  for (const page of pages) {
   const fragment = page === 'software' ? '#longevity' : '';
   const dom = new JSDOM(fs.readFileSync(path.join(root, language, page + '.html'), 'utf8'), {
    url: 'https://geniva.example/' + language + page + '.html' + fragment,
    runScripts: 'outside-only'
   });
   const { window } = dom;
   let resize, copied;
   window.matchMedia = () => ({matches:false, addEventListener:(_, callback) => {resize = callback;}});
   Object.defineProperty(window.navigator, 'clipboard', {value:{writeText:async value => {copied = value;}}, configurable:true});
   window.eval(script);
   const d = window.document;
   const toggle = d.querySelector('.menu-toggle');
   const nav = d.querySelector('.nav-links');
   const group = d.querySelector('.nav-group');
   toggle.click();
   assert.equal(toggle.getAttribute('aria-expanded'), 'true');
   assert(nav.classList.contains('open'));
   assert.equal(d.querySelector('main').inert, true);
   assert.equal(d.querySelector('footer').inert, true);
   assert.equal(group.open, true);
   assert.equal(d.activeElement, nav.querySelector('a'));
   d.dispatchEvent(new window.KeyboardEvent('keydown', {key:'Escape', bubbles:true}));
   assert.equal(toggle.getAttribute('aria-expanded'), 'false');
   assert.equal(d.querySelector('main').inert, false);
   assert.equal(d.activeElement, toggle);
   toggle.click();
   resize({matches:true});
   assert(!nav.classList.contains('open'));
   assert.equal(d.querySelector('footer').inert, false);
   toggle.click();
   const destination = nav.querySelector('.nav-sub a[href="hardware.html"]');
   destination.addEventListener('click', e => e.preventDefault());
   destination.click();
   assert.equal(toggle.getAttribute('aria-expanded'), 'false');
   assert.equal(group.open, false);
   group.open = true;
   d.body.click();
   assert.equal(group.open, false);
   group.open = true;
   d.dispatchEvent(new window.KeyboardEvent('keydown', {key:'Escape', bubbles:true}));
   assert.equal(group.open, false);
   assert.equal(d.activeElement, group.querySelector('summary'));
   for (const targetLanguage of ['en','tr']) {
    const target = new URL(d.querySelector(`[data-language][lang="${targetLanguage}"]`).href);
    assert.equal(target.pathname, '/' + (targetLanguage === 'tr' ? 'tr/' : '') + page + '.html');
    assert.equal(target.hash, fragment);
   }
   if (page === 'contact') {
    d.querySelector('.copy-email').click();
    await new Promise(resolve => setImmediate(resolve));
    assert.equal(copied,'info@gennext.bio');
    assert.match(d.querySelector('.copy-status').textContent,/copied|kopyalandı/);
    window.navigator.clipboard.writeText = async () => {throw new Error('Permission unavailable');};
    d.querySelector('.copy-email').click();
    await new Promise(resolve => setImmediate(resolve));
    assert.match(d.querySelector('.copy-status').textContent,/info@gennext.bio/);
   }
   dom.window.close();
  }
 }
 const routes = {
  solutions: {'#software':'software.html#gennext','#hardware':'hardware.html#hardware','#laboratory':'software.html#laboratory','#training':'training.html#training','#community':'software.html#community','#federation':'hardware.html#federation'},
  index: {'#community':'software.html#community','#federation':'hardware.html#federation','#laboratory':'software.html#laboratory'}
 };
 for (const prefix of ['', 'tr/']) for (const [page, fragments] of Object.entries(routes)) {
  for (const [hash,target] of Object.entries(fragments)) {
   let redirected;
   const href = 'https://geniva.example/' + prefix + page + '.html?from=bookmark' + hash;
   vm.runInNewContext(script, {
    URL,
    document:{documentElement:{lang:prefix ? 'tr' : 'en'},querySelector:()=>({dataset:{page}})},
    location:{href,hash,search:'?from=bookmark',replace:value=>{redirected=value;}}
   });
   const expected = new URL(target,href);expected.search='?from=bookmark';
   assert.equal(redirected,expected.href);
  }
 }
 for (const page of pages) {
  const html = fs.readFileSync(path.join(root,'en',page+'.html'),'utf8');
  const redirect = html.match(/<script>(.*?)<\/script>/s)[1];
  let output;
  vm.runInNewContext(redirect,{location:{search:'?from=old',hash:'#longevity',replace:value=>{output=value;}}});
  assert.equal(new URL(output,'https://geniva.example/en/'+page+'.html').href,'https://geniva.example/'+page+'.html?from=old#longevity');
 }
 console.log('PASS: DOM menu open/close, Escape, resize cleanup, dropdown, language links, clipboard success/fallback on 16 pages; 18 legacy section routes and 8 English URL redirects.');
 console.log('DOM checks only; visual layout and browser-native interactions remain unverified.');
})().catch(error=>{console.error(error);process.exitCode=1;});
