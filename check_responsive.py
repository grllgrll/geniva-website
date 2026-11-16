"""Static CSS cascade checks; these do not replace visual browser QA.
Optional QA dependencies: lxml, tinycss2, cssselect2.
"""
from pathlib import Path
import re
from lxml import html
import tinycss2, cssselect2
from build import PAGES

ROOT=Path(__file__).resolve().parent/'dist'/'client'
rules=tinycss2.parse_stylesheet((ROOT/'styles.css').read_text(),skip_comments=True,skip_whitespace=True)
assert not [r for r in rules if r.type=='error']

def active(query,width):
 query=query.strip()
 if query=='print' or 'prefers-reduced-motion' in query:return False
 return all(width<=int(v) if kind=='max' else width>=int(v) for kind,v in re.findall(r'(max|min)-width:\s*(\d+)px',query))

def matcher(width):
 m=cssselect2.Matcher()
 def add(items):
  for rule in items:
   if rule.type=='at-rule' and rule.lower_at_keyword=='media' and active(tinycss2.serialize(rule.prelude),width):
    add(tinycss2.parse_rule_list(rule.content,skip_comments=True,skip_whitespace=True))
   if rule.type=='qualified-rule':
    declarations=tinycss2.parse_declaration_list(rule.content,skip_comments=True,skip_whitespace=True)
    assert not [d for d in declarations if d.type=='error']
    selector=tinycss2.serialize(rule.prelude)
    if '::' in selector:continue
    for compiled in cssselect2.compile_selector_list(selector):
     m.add_selector(compiled,{d.lower_name:tinycss2.serialize(d.value).strip() for d in declarations if d.type=='declaration'})
 add(rules)
 return m

def style(root,selector,m):
 el=root.query(selector)
 assert el is not None,selector
 result={}
 for _,_,pseudo,decl in m.match(el):
  if pseudo is None:result.update(decl)
 return result

widths=[320,360,375,390,414,430,599,600,601,759,760,761,768,820,960,1024,1100,1101,1440]
checked=0
for width in widths:
 m=matcher(width)
 for lang in ['', 'tr/']:
  docs={p:cssselect2.ElementWrapper.from_html_root(html.fromstring((ROOT/lang/(p+'.html')).read_text())) for p in PAGES}
  for page,document in docs.items():
   viewport=document.query('meta[name="viewport"]').etree_element.get('content')
   assert 'width=device-width' in viewport and 'user-scalable=no' not in viewport
   assert style(document,'.header-contact',m)['display']=='inline-flex'
   assert style(document,'.header-contact',m)['min-height']=='44px'
   assert style(document,'.menu-toggle',m)['min-height']=='44px'
   for img in document.query_all('img'):
    declarations={}
    for _,_,pseudo,decl in m.match(img):
     if pseudo is None:declarations.update(decl)
    assert 'max-width' in declarations,(width,lang,page,'unbounded image')
   checked+=1
  root=docs['index'];nav=style(root,'.nav-links',m);toggle=style(root,'.menu-toggle',m)
  assert nav['display']==('none' if width<=1100 else 'flex'),width
  assert toggle['display']==('block' if width<=1100 else 'none'),width
  assert style(docs['contact'],'.contact-grid',m)['grid-template-columns']==('1fr' if width<=760 else '1.25fr .85fr')
  assert style(docs['contact'],'.contact-fallback',m)['grid-template-columns']==('1fr' if width<=760 else '1fr auto')
  assert style(docs['contact'],'.form-submit',m)['width']=='100%'
  assert style(docs['contact'],'.form-row',m)['grid-template-columns']==('1fr' if width<=600 else '1fr 1fr')
  assert style(docs['contact'],'.contact-demo',m).get('flex-direction','row')==('column' if width<=760 else 'row')
  assert style(docs['contact'],'.contact-demo',m)['grid-column']=='1/-1'
  assert style(docs['contact'],'.contact-product-logo',m)['height']=='auto'
  for selector in ['#contact-name','#contact-email','#contact-phone','#contact-topic','#contact-message']:
   field=style(docs['contact'],selector,m)
   assert field['min-width']=='0' and field['width']=='100%'
   assert field['font'].startswith('16px/'),(width,selector,field['font'])
   assert int(field['min-height'].removesuffix('px'))>=44
  assert style(docs['software'],'.intro-video',m)['aspect-ratio']=='16/9'
  assert style(docs['software'],'.intro-video iframe',m)['width']=='100%'
  if width<=760:
   for page,selector in [('solutions','.solution-row'),('training','.training-intro'),('careers','.detail-grid')]:
    assert style(docs[page],selector,m)['grid-template-columns']=='1fr'
  if width<=1100:
   assert nav['height']=='calc(100dvh - 74px)' and nav['overflow-y']=='auto'
   assert 'backdrop-filter' not in style(root,'.site-header',m)
   assert style(root,'.services-grid',m)['grid-template-columns']=='1fr'
   assert style(docs['hardware'],'.federation-nodes',m)['grid-template-columns']=='1fr'
  if width<=600:
   assert style(root,'.nav-tools>.language',m)['display']=='none'
   assert style(root,'.mobile-language',m)['display']=='flex'
   assert style(root,'.mobile-language a',m)['min-width']=='44px'
   assert style(root,'.service-card',m)['display']=='flex'
   assert style(docs['references'],'.logo-grid',m)['grid-template-columns']=='1fr'
   assert style(docs['software'],'.workflow',m)['grid-template-columns']=='1fr'
   assert style(docs['hardware'],'.hardware-gallery',m)['grid-template-columns']=='1fr'
   assert style(docs['about'],'.omics-layers',m)['grid-template-columns']=='1fr'
 print(f'PASS {width}px: EN/TR navigation, services, workflow, images, references, contact and omics CSS rules.')
print(f'PASS: {checked} page/width combinations across {len(widths)} widths, including responsive boundaries.')
print('Static CSS rules only: actual overflow, browser rendering, virtual keyboards and physical devices remain unverified.')
