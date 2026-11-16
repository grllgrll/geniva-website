"""Validate generated routes, languages, assets and agreed content structure."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from build import PAGES, CONTENT

class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=[];self.h1=0;self.lang=None;self.header=False;self.header_links=[];self.images=[];self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if tag=='header':self.header=True
  if tag=='h1':self.h1+=1
  if 'id' in a:self.ids.append(a['id'])
  if tag=='img':
   assert 'alt' in a,('Missing image alt',a)
   assert 'width' in a and 'height' in a,('Missing image dimensions',a)
   self.images.append(a)
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
  if self.header and tag=='a':self.header_links.append(a.get('href',''))
 def handle_endtag(self,tag):
  if tag=='header':self.header=False

root=Path(__file__).resolve().parent/'dist'/'client'
real=[];aliases=[]
for path in root.rglob('*.html'):
 text=path.read_text();page=Page(text)
 assert len(page.ids)==len(set(page.ids)),('Duplicate IDs',path)
 if path.parent.name=='en':
  aliases.append(path)
  assert 'location.replace(' in text and 'location.search+location.hash' in text
  assert f'../{path.name}' in text
 else:
  real.append(path)
  expected_lang='tr' if path.parent.name=='tr' else 'en'
  assert page.lang==expected_lang,(path,page.lang)
  assert page.h1==1,(path,page.h1)
  assert not any('gennext.bio' in href for href in page.header_links),('Header product button remains',path)
  assert f'data-page="{path.stem}"' in text
  for required in ['https://www.youtube.com/@GennextCommunity','info@gennext.bio','tel:+902162504471','TEKMER','hreflang="x-default"']:
   assert required in text,(path,required)
  for removed in ['Acıbadem Life','WeHealth','GenomiColor','Nurcivan','Murat Baş','Demet Akpolat','Muhammet İkbal Bakırcı','team-section','Ekibimiz','Meet our team','institutional reporting']:
   assert removed not in text,(path,removed)
  if path.stem!='references':assert 'insight' not in text.lower(),path
  if path.stem=='index':
   assert 'class="services-grid"' in text
   assert text.count('class="service-card"')==3
   assert 'assets/laboratory.jpg' not in text
   assert 'class="federation-visual"' not in text
   assert 'contact.html#demo' in text
  if path.stem=='solutions':assert text.count('class="solution-row"')==3
  if path.stem=='software':
   assert 'contact.html#demo' in text
   for id in ['gennext','clinical','longevity','laboratory','community']:assert id in page.ids,(path,id)
   assert text.count('assets/laboratory.jpg')==1
   assert 'youtube-nocookie.com/embed/bQ-PGMYtemI' in text
   assert 'Automated analysis' in text if expected_lang=='en' else 'Otomatik analiz' in text
  if path.stem=='hardware':assert 'federation' in page.ids and 'assets/server.webp' in text
  if path.stem=='references':
   assert text.count('class="institution-name"')==17
   assert text.count('class="citation"')==7
   assert 'Aziz Sancar' in text and 'assets/logos/detae.png' in text
   assert 'Portakal Klinik' in text and 'assets/logos/portakal.png' in text
  if path.stem=='contact':
   assert text.count('class="contact-option"')==3
   assert 'id="contact-form"' in text and 'action="/api/contact"' in text
   assert 'name="marketing_opt_in" value="yes"' in text
   for required in ['demo','career','message']:assert required in page.ids
  if path.stem=='careers':assert 'contact.html#career' in text
  assert 'class="header-contact" href="contact.html"' in text
 for value in page.links:
  url=urlsplit(value)
  if url.scheme or url.netloc:continue
  target=(path.parent/unquote(url.path)).resolve() if url.path else path
  assert target.exists(),(path,value)
  if url.fragment and target.suffix=='.html':assert url.fragment in Page(target.read_text()).ids,(path,value)
assert len(real)==18 and len(aliases)==9,(len(real),len(aliases))
assert Page((root/'index.html').read_text()).lang=='en'
for lang,d in CONTENT.items():
 for key,(title,description) in d['metadata'].items():
  assert len(title)<=60,(lang,key,'title',len(title))
  assert len(description)<=155,(lang,key,'description',len(description))
for page in PAGES:
 assert (root/'tr'/(page+'.html')).exists()
 assert (root/'en'/(page+'.html')).exists()
print('PASS: 18 content pages, 9 redirects, EN default, TR counterparts, all local links/assets/fragments, service hierarchy, reference roster and contact details.')
