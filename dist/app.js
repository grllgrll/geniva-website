(() => {
 'use strict';
 const isEnglish=document.documentElement.lang==='en';
 const toggle=document.querySelector('.menu-toggle');
 const nav=document.querySelector('.nav-links');
 const pageRegions=document.querySelectorAll('main, .site-footer');
 function setMenu(open){
  nav.classList.toggle('open',open);
  toggle.setAttribute('aria-expanded',String(open));
  toggle.textContent=open?(isEnglish?'Close':'Kapat'):(isEnglish?'Menu':'Menü');
  document.body.classList.toggle('menu-open',open);
  pageRegions.forEach(region=>{region.inert=open;});
 }
 function closeMenu(){setMenu(false);}
 toggle.addEventListener('click',()=>{
  const open=!nav.classList.contains('open');setMenu(open);
  if(open)nav.querySelector('a')?.focus({preventScroll:true});
 });
 nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',()=>{
  const wasOpen=nav.classList.contains('open');closeMenu();
  if(wasOpen)toggle.focus({preventScroll:true});
 }));
 document.addEventListener('keydown',event=>{
  if(!nav.classList.contains('open'))return;
  if(event.key==='Escape'){closeMenu();toggle.focus({preventScroll:true});}
  if(event.key==='Tab'){
   const items=[...document.querySelectorAll('.site-header a, .site-header button')].filter(el=>el.getClientRects().length);
   const first=items[0],last=items[items.length-1];
   if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}
   else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}
  }
 });
 window.matchMedia('(min-width: 961px)').addEventListener('change',event=>{if(event.matches)closeMenu();});
 const dialog=document.querySelector('.dialog');
 if(dialog){let opener=null;document.querySelectorAll('[data-zoom]').forEach(button=>button.addEventListener('click',()=>{opener=button;dialog.showModal();document.body.style.overflow='hidden';}));dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());dialog.addEventListener('close',()=>{document.body.style.overflow='';opener?.focus();});dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});}
 const copy=document.querySelector('.copy-email');
 if(copy)copy.addEventListener('click',async()=>{const status=document.querySelector('.copy-status');try{await navigator.clipboard.writeText('info@gennext.bio');status.textContent=isEnglish?'Email address copied.':'E-posta adresi kopyalandı.';}catch{status.textContent=isEnglish?'Select and copy this address: info@gennext.bio':'Bu adresi seçerek kopyalayabilirsiniz: info@gennext.bio';}});
 document.querySelectorAll('[data-language]').forEach(link=>{if(location.hash)link.href+=location.hash;});
})();
