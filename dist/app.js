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
 window.matchMedia('(min-width: 961px)').addEventListener('change', event => { if (event.matches) setMenu(false); });
 const languageLinks = [...document.querySelectorAll('[data-language]')];
 function syncLanguageLinks() {
  languageLinks.forEach(anchor => { const url = new URL(anchor.href); url.hash = location.hash; anchor.href = url.href; });
 }
 syncLanguageLinks();
 window.addEventListener('hashchange', () => { if (!redirectLegacySection()) syncLanguageLinks(); });
 const copy = document.querySelector('.copy-email');
 copy?.addEventListener('click', async () => {
  const status = document.querySelector('.copy-status');
  try { await navigator.clipboard.writeText('info@gennext.bio'); status.textContent = english ? 'Email address copied.' : 'E-posta adresi kopyalandı.'; }
  catch { status.textContent = english ? 'Select and copy this address: info@gennext.bio' : 'Bu adresi seçerek kopyalayabilirsiniz: info@gennext.bio'; }
 });
})();
