from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.ids=set();self.h1=0;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='img':assert 'alt' in a, 'Missing image alt'
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
root=Path(__file__).resolve().parent/'dist'
count=0
for p in root.rglob('*.html'):
 text=p.read_text();page=Page(text)
 assert page.h1==1,p
 assert 'team-section' not in text and 'Ekibimiz' not in text and 'Meet our team' not in text,p
 for required in ['https://www.youtube.com/@GennextCommunity','info@gennext.bio','tel:+902165004471','TEKMER']:
  assert required in text,(p,required)
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(p.parent/unquote(u.path)).resolve() if u.path else p
  assert target.exists(),(p,link)
  if u.fragment and target.suffix=='.html':assert u.fragment in Page(target.read_text()).ids,(p,link)
 count+=1
assert count==8,count
print(f'{count} pages: local assets, links, fragments, headings, contact details and team removal OK.')
