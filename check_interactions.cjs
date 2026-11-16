// DOM-level interaction checks. Requires jsdom; no browser rendering is performed.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const { JSDOM } = require(process.env.GENIVA_QA_MODULES ? path.join(process.env.GENIVA_QA_MODULES, 'jsdom') : 'jsdom');
const root = path.join(__dirname, 'dist', 'client');
const script = fs.readFileSync(path.join(root, 'app.js'), 'utf8');
const pages = ['index','solutions','software','hardware','training','about','references','careers','contact'];
(async () => {
 for (const language of ['', 'tr/']) {
  for (const page of pages) {
   const fragment = page === 'software' ? '#longevity' : '';
   const dom = new JSDOM(fs.readFileSync(path.join(root, language, page + '.html'), 'utf8'), {
    url: 'https://geniva.example/' + language + page + '.html' + fragment,
    runScripts: 'outside-only'
   });
   const { window } = dom;
   let resize, copied, scrolled;
   window.HTMLElement.prototype.scrollIntoView = function () {scrolled = this.id;};
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
   // Model visible focus targets; jsdom itself does not render their rectangles.
   const focusTargets = [...d.querySelectorAll('.site-header a, .site-header button, .site-header summary')];
   focusTargets.forEach(el => {el.getClientRects = () => [{}];});
   const first = focusTargets[0], last = focusTargets.at(-1);
   last.focus();
   d.dispatchEvent(new window.KeyboardEvent('keydown', {key:'Tab',bubbles:true,cancelable:true}));
   assert.equal(d.activeElement, first);
   d.dispatchEvent(new window.KeyboardEvent('keydown', {key:'Tab',shiftKey:true,bubbles:true,cancelable:true}));
   assert.equal(d.activeElement, last);
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
    const form = d.querySelector('#contact-form'), topic = form.elements.topic;
    assert.equal(form.elements.marketing_opt_in.checked, false);
    assert.equal(form.elements.marketing_opt_in.required, false);
    assert.equal(form.querySelector('.form-submit').disabled, false);
    assert.equal(d.querySelector('.header-contact').textContent, language ? 'İletişim' : 'Contact Us');
    for (const card of d.querySelectorAll('[data-contact-topic]')) {
     assert.equal(new URL(card.href).protocol, 'mailto:');
     card.click();
     assert.equal(topic.value, card.dataset.topicValue || card.id);
     assert.equal(d.querySelectorAll('.contact-option[aria-current]').length, 1);
     assert.equal(d.activeElement, d.querySelector('[data-form-heading]'));
     assert.notEqual(d.activeElement.tagName, 'INPUT');
     assert.equal(scrolled, 'message');
     for (const anchor of d.querySelectorAll('[data-language]')) assert.equal(new URL(anchor.href).hash, '#' + (card.dataset.topicValue || card.id));
    }
    window.location.hash = '#demo';
    await new Promise(resolve => setTimeout(resolve, 5));
    assert.equal(topic.value, 'demo');
    assert.match(d.querySelector('[data-form-heading]').textContent, /demo/);
    assert.equal(d.querySelector('[data-demo-brand]').hidden, false);
    assert.equal(d.querySelector('[data-topic-value="demo"]').getAttribute('aria-current'), 'true');
    topic.value = 'career';topic.dispatchEvent(new window.Event('change'));
    assert.equal(form.querySelector('[data-career-field]').hidden, false);
    assert.equal(form.elements.portfolio_url.disabled, false);
    assert.equal(d.querySelector('[data-demo-brand]').hidden, true);
    topic.value = 'general';topic.dispatchEvent(new window.Event('change'));
    assert.equal(form.elements.portfolio_url.disabled, true);
    const call = form.querySelector('[name="reply_by"][value="phone"]');call.click();
    assert.equal(form.elements.phone.required, true);
    form.querySelector('[name="reply_by"][value="email"]').click();
    assert.equal(form.elements.phone.required, false);
    let sent = [], fail = true;
    window.fetch = async (url,options) => {sent.push(JSON.parse(options.body));return {ok:!fail,json:async()=>fail?{error:'unavailable'}:{ok:true}};};
    form.elements.name.value = 'QA Example';form.elements.email.value = 'qa@example.test';form.elements.message.value = 'This is a local DOM check.';
    form.dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve => setImmediate(resolve));
    assert.equal(sent.length,1);assert.equal(sent[0].marketing_opt_in,false);
    assert(form.querySelector('.form-status').classList.contains('error'));
    assert.equal(form.elements.message.value, 'This is a local DOM check.');
    fail = false;
    form.dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve => setImmediate(resolve));
    assert.equal(sent.length,2);assert.equal(sent[0].id,sent[1].id);
    assert(form.querySelector('.form-status').classList.contains('success'));
    assert.equal(form.elements.message.value,'');
    assert.equal(form.elements.marketing_opt_in.checked,false);
    form.elements.name.value='QA Again';form.elements.email.value='qa@example.test';form.elements.message.value='This tests explicit consent.';form.elements.marketing_opt_in.checked=true;
    form.dispatchEvent(new window.Event('submit',{cancelable:true}));
    await new Promise(resolve => setImmediate(resolve));
    assert.equal(sent[2].marketing_opt_in,true);assert.notEqual(sent[1].id,sent[2].id);
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
 console.log('PASS: menu, language links, contact topics, demo/career, callback validation, form submission/retry and consent and clipboard success/fallback; 18 pages, 18 legacy section routes and 9 redirects.');
 console.log('DOM checks only; visual layout and browser-native interactions remain unverified.');
})().catch(error=>{console.error(error);process.exitCode=1;});
