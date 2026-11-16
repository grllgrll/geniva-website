(() => {
 'use strict';
 const english = document.documentElement.lang === 'en';
 const page = document.querySelector('main')?.dataset.page;
 const legacyRoutes = {
  solutions: {'#software':'software.html#gennext','#hardware':'hardware.html#hardware','#laboratory':'software.html#laboratory','#training':'training.html#training','#community':'software.html#community','#federation':'hardware.html#federation'},
  index: {'#community':'software.html#community','#federation':'hardware.html#federation','#laboratory':'software.html#laboratory'}
 };
 function redirectLegacySection() {
  const route = legacyRoutes[page]?.[location.hash];
  if (!route) return false;
  const destination = new URL(route, location.href);
  destination.search = location.search;
  location.replace(destination.href);
  return true;
 }
 if (redirectLegacySection()) return;
 const toggle = document.querySelector('.menu-toggle');
 const nav = document.querySelector('.nav-links');
 const group = document.querySelector('.nav-group');
 const pageRegions = document.querySelectorAll('main, .site-footer');
 function setMenu(open, restoreFocus = false) {
  nav.classList.toggle('open', open);
  toggle.setAttribute('aria-expanded', String(open));
  toggle.textContent = open ? (english ? 'Close' : 'Kapat') : (english ? 'Menu' : 'Menü');
  document.body.classList.toggle('menu-open', open);
  pageRegions.forEach(region => { region.inert = open; });
  group.open = open;
  if (restoreFocus) toggle.focus({preventScroll:true});
 }
 toggle.addEventListener('click', () => {
  const open = !nav.classList.contains('open');
  setMenu(open);
  if (open) nav.querySelector('a').focus({preventScroll:true});
 });
 nav.querySelectorAll('a').forEach(anchor => anchor.addEventListener('click', () => {
  setMenu(false, nav.classList.contains('open'));
 }));
 document.addEventListener('click', event => {
  if (!nav.classList.contains('open') && !group.contains(event.target)) group.open = false;
 });
 document.addEventListener('keydown', event => {
  const open = nav.classList.contains('open');
  if (event.key === 'Escape') {
   if (open) setMenu(false, true);
   else if (group.open) { group.open = false; group.querySelector('summary').focus(); }
  }
  if (open && event.key === 'Tab') {
   const items = [...document.querySelectorAll('.site-header a, .site-header button, .site-header summary')].filter(el => el.getClientRects().length);
   const first = items[0], last = items[items.length - 1];
   if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
   else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  }
 });
 window.matchMedia('(min-width: 1101px)').addEventListener('change', event => { if (event.matches) setMenu(false); });
 const languageLinks = [...document.querySelectorAll('[data-language]')];
 function syncLanguageLinks() {
  languageLinks.forEach(anchor => { const url = new URL(anchor.href); url.hash = location.hash; anchor.href = url.href; });
 }
 syncLanguageLinks();
 const contactTopics = [...document.querySelectorAll('[data-contact-topic]')];
 const form = document.querySelector('#contact-form');
 if (form) {
  const topic = form.elements.topic, phone = form.elements.phone;
  const status = form.querySelector('.form-status'), submit = form.querySelector('.form-submit');
  const careerField = form.querySelector('[data-career-field]');
  const heading = document.querySelector('[data-form-heading]');
  let pending = false, lastPayload = '', requestId = '';
  submit.disabled = false;
  function updateTopic(focus = false) {
   contactTopics.forEach(anchor => {
    if (anchor.id === topic.value) anchor.setAttribute('aria-current', 'true');
    else anchor.removeAttribute('aria-current');
   });
   careerField.hidden = topic.value !== 'career';
   form.elements.portfolio_url.disabled = careerField.hidden;
   heading.textContent = topic.value === 'demo' ? (english ? 'Book a Gennext demo.' : 'Gennext demosu talep edin.') : topic.value === 'career' ? (english ? 'Introduce yourself.' : 'Kendinizi tanıtın.') : (english ? 'Send a message. Let’s talk.' : 'Bize yazın. Görüşelim.');
   form.elements.message.placeholder = topic.value === 'demo' ? (english ? 'What would you like to explore in Gennext? Tell us about your team and availability.' : 'Gennext’te hangi alanı incelemek istersiniz? Ekibinizi ve uygun olduğunuz zamanı paylaşın.') : topic.value === 'career' ? (english ? 'Tell us about your experience, interests and how you would like to contribute.' : 'Deneyiminizi, ilgi alanlarınızı ve nasıl katkıda bulunmak istediğinizi anlatın.') : (english ? 'A few words about your needs, team or project.' : 'İhtiyacınız, ekibiniz veya projeniz hakkında birkaç cümle.');
   if (focus) {form.elements.name.focus({preventScroll:true});document.querySelector('#message').scrollIntoView({block:'start'});}
  }
  function syncReply() {
   const call = form.elements.reply_by.value === 'phone';
   phone.required = call;
   form.querySelector('[data-phone-optional]').hidden = call;
   form.querySelector('[data-phone-required]').hidden = !call;
  }
  function selectTopicFromHash() {
   const value = location.hash.slice(1);
   if ([...topic.options].some(option => option.value === value)) topic.value = value;
   updateTopic();
  }
  function setTopicHash() {const url = new URL(location.href);url.hash = topic.value;history.replaceState(null, '', url);syncLanguageLinks();}
  contactTopics.forEach(anchor => anchor.addEventListener('click', event => {
   if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) return;
   event.preventDefault();topic.value = anchor.id;updateTopic(true);setTopicHash();
  }));
  topic.addEventListener('change', () => {updateTopic();setTopicHash();});
  form.querySelectorAll('[name="reply_by"]').forEach(radio => radio.addEventListener('change', syncReply));
  window.addEventListener('hashchange', selectTopicFromHash);
  selectTopicFromHash();syncReply();
  form.addEventListener('input', () => {if(!pending)submit.disabled=false;});
  form.addEventListener('submit', async event => {
   event.preventDefault();if(pending || !form.reportValidity())return;
   const payload = Object.fromEntries(new FormData(form));
   payload.marketing_opt_in = form.elements.marketing_opt_in.checked;
   payload.language = english ? 'en' : 'tr';
   const fingerprint = JSON.stringify(payload);
   if (fingerprint !== lastPayload) {requestId = crypto.randomUUID();lastPayload = fingerprint;}
   payload.id = requestId;
   pending=true;submit.disabled=true;form.setAttribute('aria-busy','true');
   status.className='form-status';status.textContent=english?'Sending your message…':'Mesajınız gönderiliyor…';
   const controller=new AbortController(), timer=setTimeout(()=>controller.abort(),20000);
   try {
    const response=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload),signal:controller.signal});
    const result=await response.json();
    if(!response.ok || !result.ok) {
     const message=result.error==='rate_limit' ? (english?'You’ve sent several messages recently. Please try again later, email us or call us.':'Kısa sürede birkaç mesaj gönderdiniz. Lütfen daha sonra tekrar deneyin, e-posta yazın veya bizi arayın.') : result.error==='phone' ? (english?'Please enter a phone number so we can call you.':'Sizi arayabilmemiz için telefon numaranızı girin.') : (english?'Your message could not be sent. Please try again, email info@gennext.bio or call +90 216 250 4471.':'Mesajınız gönderilemedi. Tekrar deneyin, info@gennext.bio adresine yazın veya +90 216 250 4471 numarasını arayın.');
     throw new Error(message);
    }
    const selected=topic.value, call=payload.reply_by==='phone';
    form.reset();topic.value=selected;updateTopic();syncReply();lastPayload='';requestId='';
    status.className='form-status success';
    status.textContent=selected==='demo' ? (english?'Your demo request has been received. We’ll contact you to arrange a suitable time.':'Demo talebiniz alındı. Uygun bir zaman belirlemek için sizinle iletişime geçeceğiz.') : selected==='career' ? (english?'Your application has been received. Thank you for introducing yourself.':'Başvurunuz alındı. Kendinizi tanıttığınız için teşekkür ederiz.') : call ? (english?'Your message has been received. We’ll call you at the number you shared.':'Mesajınız alındı. Paylaştığınız numaradan sizi arayacağız.') : (english?'Your message has been received. We’ll reply to your email address.':'Mesajınız alındı. E-posta adresinize yanıt vereceğiz.');
    status.focus({preventScroll:true});status.scrollIntoView({block:'nearest'});
   } catch(error) {
    status.className='form-status error';
    status.textContent = error.name==='AbortError' || error instanceof TypeError ? (english?'We couldn’t confirm delivery. Your message is still here; retry to check or use email or phone below.':'Gönderimi doğrulayamadık. Mesajınız burada duruyor; tekrar deneyebilir, e-posta yazabilir veya bizi arayabilirsiniz.') : error.message;
    submit.disabled=false;status.focus({preventScroll:true});
   } finally {clearTimeout(timer);pending=false;form.removeAttribute('aria-busy');}
  });
 }
 window.addEventListener('hashchange', () => {if(!redirectLegacySection())syncLanguageLinks();});
 const copy = document.querySelector('.copy-email');
 copy?.addEventListener('click', async () => {
  const status = document.querySelector('.copy-status');
  try { await navigator.clipboard.writeText('info@gennext.bio'); status.textContent = english ? 'Email address copied.' : 'E-posta adresi kopyalandı.'; }
  catch { status.textContent = english ? 'Select and copy this address: info@gennext.bio' : 'Bu adresi seçerek kopyalayabilirsiniz: info@gennext.bio'; }
 });
})();
