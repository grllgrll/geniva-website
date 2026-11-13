"""Product imagery, federation explanation and publication presentation."""
import json

def screen(d,p):
 return f'''<figure class="product-illustration"><img src="{p}assets/gennext-product.webp" width="1672" height="941" alt="{pick(d,'Gennext analiz ekranının stilize temsili: kalite kontrol, filtreler ve varyant değerlendirme tablosu','Stylised Gennext analysis screen with quality control, filters and a variant assessment table')}" loading="lazy"><figcaption>{pick(d,'Gennext arayüzünün stilize gösterimi.','A stylised view of the Gennext interface.')}</figcaption></figure>'''

def hardware(d,p):
 items=[('hardware.jpg','Worker Node',pick(d,'Kurum içi analiz istasyonu','On-site analysis workstation')),('server.webp',pick(d,'Yüksek hacimli sunucu','High-throughput server'),pick(d,'Yoğun ve eş zamanlı analiz iş yükleri için','For intensive and concurrent analysis workloads'))]
 return '<div class="hardware-gallery">'+''.join(f'<figure><div class="hardware-image"><img src="{p}assets/{file}" width="1024" height="1024" alt="{title}" loading="lazy"></div><figcaption><h3>{title}</h3><p>{desc}</p></figcaption></figure>' for file,title,desc in items)+'</div>'

DB='<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><ellipse cx="20" cy="9" rx="12" ry="5"/><path d="M8 9v20c0 7 24 7 24 0V9M8 19c0 7 24 7 24 0"/></svg>'
REPORT='<svg viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M10 3h15l6 7v27H10zM25 3v8h6M15 18h11M15 24h11M15 30h7"/></svg>'
LOCK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="5" y="10" width="14" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3M12 14v3"/></svg>'

def diagram(d):
 nodes=''
 for name in pick(d,['Kurum A','Kurum B','Kurum C'],['Institution A','Institution B','Institution C']):
  nodes+=f'''<article class="federation-node"><h4>{name}</h4><p class="local-label">{pick(d,'KURUMUN YEREL ALTYAPISI','LOCAL INFRASTRUCTURE')}</p><div class="local-pipeline"><span>{DB}<strong>{pick(d,'Genomik veri','Genomic data')}</strong></span><b aria-hidden="true">→</b><span>{icon('hardware')}<strong>Worker Node</strong></span><b aria-hidden="true">→</b><span>{REPORT}<strong>{pick(d,'Analiz çıktısı','Analysis output')}</strong></span></div><div class="local-retention">{LOCK}<span>{pick(d,'Veri ve hesaplama kurumda kalır','Data and computing stay on site')}</span></div></article>'''
 return f'''<figure class="federation-visual" id="federation"><div class="federation-heading"><span>GENNEXT</span><strong>{pick(d,'Tek platform. Dağıtık analiz gücü.','One platform. Distributed analysis.')}</strong></div><div class="federation-coordinator"><span class="coordinator-icon">{icon('software')}</span><div><h3>{pick(d,'Merkezi koordinasyon','Central coordination')}</h3><p>{pick(d,'Kullanıcı erişimi · Görev atama · İşlem durumu','User access · Task assignment · Workflow status')}</p></div></div><div class="coordination-lane"><span aria-hidden="true">↓ ↑</span><p>{pick(d,'Analiz görevi ve durum bilgisi','Analysis tasks and status information')}</p></div><div class="federation-nodes">{nodes}</div><figcaption><span class="legend-local"></span>{pick(d,'Genomik girdiler ve analiz çıktıları yerelde işlenir.','Genomic inputs and analysis outputs are processed locally.')}<br><span class="legend-control"></span>{pick(d,'Koordinasyon için gerekli erişim, görev ve süreç üst verileri merkezi hizmetlerle paylaşılır.','Access, task and workflow metadata required for coordination are shared with central services.')}</figcaption></figure>'''

previous_laboratory=laboratory
def laboratory(d,p,compact=False):
 if compact:return previous_laboratory(d,p,True)
 return f'''<section class="section lab-section" id="laboratory"><div class="container"><div class="section-head"><div><p class="eyebrow">{pick(d,'LONGEVITY LABORATUVARI','LONGEVITY LABORATORY')}</p><h2>{pick(d,'Laboratuvardan<br>kişisel sağlık verisine.','From the laboratory<br>to personal health insights.')}</h2></div><p>{pick(d,'Kendi laboratuvarımızda microarray ve uzun okuma dizileme çalışmaları yürütüyoruz. Bu altyapıyı longevity hizmetlerimizin genetik ve epigenetik değerlendirmelerinde kullanıyoruz.','Our laboratory performs microarray and long-read sequencing work, supporting genetic and epigenetic assessment within our longevity services.')}</p></div><div class="lab-content"><figure class="lab-photo"><img src="{p}assets/laboratory.jpg" width="600" height="338" alt="{pick(d,'Geniva laboratuvarının çalışma alanı','Geniva laboratory workspace')}" loading="lazy"></figure><div class="lab-services"><article><p class="eyebrow">MICROARRAY</p><h3>{pick(d,'Genetik ve epigenetik profilleme','Genetic and epigenetic profiling')}</h3><p>{pick(d,'Genotipleme ve DNA metilasyonu çalışmalarıyla genetik yatkınlık ve epigenetik değerlendirmelere veri sağlıyoruz.','Genotyping and DNA methylation workflows provide data for genetic predisposition and epigenetic assessment.')}</p></article><article><p class="eyebrow">LONG-READ</p><h3>{pick(d,'Uzun okuma dizileme','Long-read sequencing')}</h3><p>{pick(d,'Nanopore teknolojisiyle uzun DNA parçalarını diziliyor, elde edilen verileri çalışmanın amacına uygun analiz ediyoruz.','We sequence long DNA fragments with Nanopore technology and analyse the resulting data for the aims of each study.')}</p></article></div></div>{link(pick(d,'Laboratuvar hizmetlerini konuşalım','Discuss laboratory services'),'contact.html','button navy')}</div></section>'''

def community(d,p):
 return f'''<section class="section community-section" id="community"><div class="container"><div class="section-head"><div><p class="eyebrow">GENNEXT</p><h2>{pick(d,'Gennext’i yakından tanıyın.','Get to know Gennext.')}</h2></div><p>{pick(d,'Platformu tanıtım videomuzda keşfedin. Kullanım eğitimleri ve analiz iş akışları için Gennext Community kanalımızı ziyaret edin.','Discover the platform in our introduction video. Visit Gennext Community for tutorials and analysis workflows.')}</p></div><div class="intro-video"><iframe src="https://www.youtube-nocookie.com/embed/bQ-PGMYtemI" title="{pick(d,'Gennext tanıtım videosu','Gennext introduction video')}" width="1120" height="630" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div><div class="video-links">{link(pick(d,'Videoyu YouTube’da açın','Watch on YouTube'),'https://www.youtube.com/watch?v=bQ-PGMYtemI',external=True)}{link(d['learnButton'],CHANNEL,external=True)}</div></div></section>'''

# Loaded after asset collection; source URLs remain in the data file for maintenance.
data_path=ROOT/'assets/reference-data.json'
REFERENCE_DATA=json.loads(data_path.read_text()) if data_path.exists() else {}

def reference_name(name,p):
 info=REFERENCE_DATA.get('logos',{}).get(name)
 if not info:return f'<span class="institution-name">{escape(name)}</span>'
 path=info['asset']
 theme=' logo-dark' if info.get('dark') else ''
 return f'<span class="institution-logo{theme}"><img src="{p}{path}" alt="" loading="lazy"></span><span class="institution-name">{escape(name)}</span>'

def references(d,p):
 groups=''
 for group,names in REFERENCE_GROUPS:
  branded=[name for name in names if name in REFERENCE_DATA.get('logos',{})]
  plain=[name for name in names if name not in REFERENCE_DATA.get('logos',{})]
  title=pick(d,'Somatik','Somatic') if group=='Somatik / Somatic' else group
  logos='<ul class="logo-grid">'+''.join(f'<li>{reference_name(name,p)}</li>' for name in branded)+'</ul>'
  textrefs='<ul class="plain-references">'+''.join(f'<li>{escape(name)}</li>' for name in plain)+'</ul>' if plain else ''
  groups+=f'<article class="reference-group"><h3>{title}</h3>{logos}{textrefs}</article>'
 pubs=''
 for kind,title,meta,tr,en,url in PUBS:
  info=REFERENCE_DATA.get('citations',{}).get(url,{})
  authors=info.get('authors',meta.split(' · ')[0])
  journal=info.get('journal',meta.split(' · ')[1])
  detail=info.get('details',meta.split(' · ')[2]+'.')
  suffix=pick(d,' [Ön baskı]',' [Preprint]') if kind=='preprint' else (pick(d,' [Bildiri özeti]',' [Conference abstract]') if kind=='abstract' else '')
  doi=url.replace('https://doi.org/','') if 'doi.org/' in url else ''
  citation=f'{escape(authors)} {escape(title)}. <i>{escape(journal)}</i> {escape(detail)}'
  pubs+=f'<article class="publication citation"><p>{citation}</p>{link("doi: "+doi if doi else pick(d,"Yayını görüntüle","View publication"),url,external=True)}</article>'
 return f'''<main id="main">{innerhero(d,pick(d,'Kurumlarla birlikte.<br>Bilimsel çalışmaların içinde.','Working with institutions.<br>Contributing to research.'),pick(d,'Klinik genomik ve longevity alanındaki referanslarımız ile Gennext’in kullanıldığı bilimsel çalışmalardan seçkiler.','Our clinical genomics and longevity references, alongside selected scientific studies using Gennext.'),'references')}<section class="section"><div class="container"><p class="eyebrow">{pick(d,'ÇALIŞTIĞIMIZ KURUMLAR VE PROFESYONELLER','INSTITUTIONS & PROFESSIONALS')}</p><h2>{pick(d,'Farklı ihtiyaçlar,<br>ortak çalışma alanları.','Different needs.<br>Shared areas of work.')}</h2><div class="reference-groups reference-logos">{groups}</div></div></section><section class="section product-band" id="publications"><div class="container"><p class="eyebrow">{pick(d,'BİLİMSEL YAYINLAR','SCIENTIFIC PUBLICATIONS')}</p><h2>{pick(d,'Araştırmalarda Gennext','Gennext in research')}</h2><p class="publication-intro">{pick(d,'Gennext’in kullanıldığı bilimsel çalışmalardan seçkiler.','Selected scientific studies using Gennext.')}</p><div class="citation-list">{pubs}</div></div></section>{cta(d)}</main>'''

RENDERERS['references']=references
