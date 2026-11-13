(() => {
 'use strict';
 const isEnglish=document.documentElement.lang==='en';
 const toggle=document.querySelector('.menu-toggle');
 const nav=document.querySelector('.nav-links');
 function closeMenu(){nav.classList.remove('open');toggle.setAttribute('aria-expanded','false');toggle.textContent=isEnglish?'Menu':'Menü';document.body.classList.remove('menu-open');}
 toggle.addEventListener('click',()=>{const open=nav.classList.toggle('open');toggle.setAttribute('aria-expanded',String(open));toggle.textContent=open?(isEnglish?'Close':'Kapat'):(isEnglish?'Menu':'Menü');document.body.classList.toggle('menu-open',open);});
 nav.querySelectorAll('a').forEach(link=>link.addEventListener('click',closeMenu));
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&nav.classList.contains('open')){closeMenu();toggle.focus();}});
 window.matchMedia('(min-width: 761px)').addEventListener('change',event=>{if(event.matches)closeMenu();});
 const dialog=document.querySelector('.dialog');
 if(dialog){let opener=null;document.querySelectorAll('[data-zoom]').forEach(button=>button.addEventListener('click',()=>{opener=button;dialog.showModal();document.body.style.overflow='hidden';}));dialog.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());dialog.addEventListener('close',()=>{document.body.style.overflow='';opener?.focus();});dialog.addEventListener('click',event=>{if(event.target===dialog){const r=dialog.getBoundingClientRect();if(event.clientX<r.left||event.clientX>r.right||event.clientY<r.top||event.clientY>r.bottom)dialog.close();}});}
 const copy=document.querySelector('.copy-email');
 if(copy)copy.addEventListener('click',async()=>{const status=document.querySelector('.copy-status');try{await navigator.clipboard.writeText('info@gennext.bio');status.textContent=isEnglish?'Email address copied.':'E-posta adresi kopyalandı.';}catch{status.textContent=isEnglish?'Select and copy this address: info@gennext.bio':'Bu adresi seçerek kopyalayabilirsiniz: info@gennext.bio';}});
 document.querySelectorAll('[data-language]').forEach(link=>{if(location.hash)link.href+=location.hash;});
})();
