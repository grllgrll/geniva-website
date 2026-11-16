"""Page copy and semantic templates. Product facts are supplied by Geniva."""
from html import escape as esc
from urllib.parse import quote

CHANNEL = 'https://www.youtube.com/@GennextCommunity'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg>'
OUT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 18 18 6M6 6h12v12"/></svg>'
ICONS = {
 'software':'<rect x="3" y="4" width="26" height="23" rx="3"/><path d="M3 10h26M10 10v17M15 17h9M15 21h6"/>',
 'hardware':'<rect x="4" y="3" width="24" height="11" rx="2"/><rect x="4" y="18" width="24" height="11" rx="2"/><path d="M9 8h1m5 0h8M9 23h1m5 0h8"/>',
 'training':'<path d="m2 11 14-7 14 7-14 7-14-7Zm5 3v10c6 5 12 5 18 0V14m5-3v13"/>',
 'data':'<ellipse cx="16" cy="7" rx="11" ry="4"/><path d="M5 7v18c0 6 22 6 22 0V7M5 16c0 6 22 6 22 0"/>',
 'report':'<path d="M8 3h12l6 6v21H8zM20 3v7h6M12 16h10M12 21h10M12 26h6"/>',
 'lock':'<rect x="6" y="14" width="20" height="15" rx="3"/><path d="M10 14V9a6 6 0 0 1 12 0v5M16 20v4"/>',
}

def t(lang, en, tr): return tr if lang == 'tr' else en

def icon(name):
 return f'<svg class="icon" viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'

def link(label, href, style='text-link', external=False):
 attrs = ' target="_blank" rel="noopener"' if external else ''
 return f'<a class="{style}" href="{esc(href,quote=True)}"{attrs}><span>{esc(label)}</span>{OUT if external else ARROW}</a>'

def contact_link(label, area, style='button'):
 return link(label, 'contact.html#' + area, style)

def image(prefix, file, alt, width, height, cls=''):
 return f'<img class="{cls}" src="{prefix}assets/{file}" alt="{esc(alt,quote=True)}" width="{width}" height="{height}" loading="lazy">'

CONTENT = {
 'en': {
  'names':dict(index='Home',solutions='Solutions',software='Software',hardware='Hardware',training='Training',about='About',references='References',contact='Contact'),
  'tagline':'Software, hardware and training for health big data.',
  'subline':'We develop software, build computing infrastructure and provide training for health data analysis, interpretation and reporting.',
  'menu':'Menu','skip':'Skip to content','language':'Language selection','navigation':'Main navigation','company':'Company','brochure':'Gennext brochure','map':'Get directions','rights':'All rights reserved.',
  'metadata':{
   'index':('Geniva | Software, Hardware & Training for Health Big Data','Software, computing infrastructure and training for health data analysis, interpretation and reporting. Explore Geniva and the Gennext platform.'),
   'solutions':('Solutions | Software, Hardware & Training | Geniva','Explore Geniva’s software, on-site computing infrastructure and training for health data analysis and reporting.'),
   'software':('Software & Reporting | Gennext by Geniva','Discover Gennext, Geniva’s software platform for clinical genomics and longevity analysis, automation and reporting.'),
   'hardware':('Hardware & Computing Infrastructure | Geniva','Worker Nodes, high-throughput servers and on-site computing infrastructure planned around your health data workloads.'),
   'training':('Training & Workshops | Geniva','Explore training in genomic data analysis, germline and somatic variant interpretation, and practical Gennext workflows.'),
   'about':('About Geniva | Health Data Technology','Geniva brings software, computing infrastructure and scientific expertise together for health data analysis, interpretation and reporting.'),
   'references':('References & Scientific Publications | Geniva','Explore Geniva’s clinical genomics and longevity references, and selected scientific publications using Gennext.'),
   'contact':('Contact Geniva | Software, Hardware & Training','Contact Geniva to discuss software and reporting, computing infrastructure, or training. Based at Acıbadem University TEKMER, Istanbul.'),
  }
 },
 'tr': {
  'names':dict(index='Ana sayfa',solutions='Çözümler',software='Yazılım',hardware='Donanım',training='Eğitim',about='Hakkımızda',references='Referanslar',contact='İletişim'),
  'tagline':'Büyük sağlık verileri için yazılım, donanım ve eğitim.',
  'subline':'Sağlık verilerinin analizi, yorumlanması ve raporlanması için yazılım geliştiriyor, hesaplama altyapısı kuruyor ve eğitim veriyoruz.',
  'menu':'Menü','skip':'İçeriğe geç','language':'Dil seçimi','navigation':'Ana menü','company':'Geniva','brochure':'Gennext broşürü','map':'Yol tarifi alın','rights':'Tüm hakları saklıdır.',
  'metadata':{
   'index':('Geniva | Sağlık Verileri için Yazılım, Donanım ve Eğitim','Sağlık verilerinin analizi, yorumlanması ve raporlanması için yazılım, hesaplama altyapısı ve eğitim. Geniva ve Gennext platformunu keşfedin.'),
   'solutions':('Çözümler | Yazılım, Donanım ve Eğitim | Geniva','Sağlık verilerinin analizi ve raporlanması için Geniva’nın yazılım, kurum içi hesaplama altyapısı ve eğitim çözümlerini inceleyin.'),
   'software':('Yazılım ve Raporlama | Geniva’nın Ürünü Gennext','Geniva’nın yazılım ürünü Gennext: klinik genomik ve longevity için veri analizi, otomasyon ve raporlama.'),
   'hardware':('Donanım ve Hesaplama Altyapısı | Geniva','Sağlık verisi iş yükünüze göre planlanan Worker Node, yüksek hacimli sunucu ve kurum içi hesaplama altyapısı.'),
   'training':('Eğitim ve Atölyeler | Geniva','Genomik veri analizi, germline ve somatik varyant değerlendirme ile uygulamalı Gennext eğitimlerini inceleyin.'),
   'about':('Geniva Hakkında | Sağlık Verileri ve Teknoloji','Geniva, sağlık verilerinin analizi, yorumlanması ve raporlanması için yazılımı, hesaplama altyapısını ve bilimsel uzmanlığı bir araya getirir.'),
   'references':('Referanslar ve Bilimsel Yayınlar | Geniva','Geniva’nın klinik genomik ve longevity referansları ile Gennext’in kullanıldığı bilimsel yayınlardan seçkiler.'),
   'contact':('İletişim | Yazılım, Donanım ve Eğitim | Geniva','Yazılım, raporlama, hesaplama altyapısı ve eğitim ihtiyaçlarınız için Geniva’ya ulaşın. Acıbadem Üniversitesi TEKMER, İstanbul.'),
  }
 }
}

SERVICES = {
 'en':[
  dict(key='software',title='Software',lead='Analysis, interpretation and reporting.',body='Gennext, our software platform, connects data processing, evaluation and reporting for clinical genomics and longevity.',scope=['Gennext platform','Clinical genomics','Longevity analysis & reporting'],cta='Explore software',need='For teams working with complex health data.',delivery='Software tools and automated workflows that bring analysis and reporting into one platform.'),
  dict(key='hardware',title='Hardware',lead='Computing power, at your institution.',body='Worker Nodes and server infrastructure configured for your data volumes, analysis workloads and existing environment.',scope=['Worker Nodes','High-throughput servers','On-site computing & storage'],cta='Explore hardware',need='For organisations that need their own analysis capacity.',delivery='Computing and storage infrastructure planned around the way your team works.'),
  dict(key='training',title='Training',lead='Build the skills behind the analysis.',body='Training in genomic analysis, variant interpretation and practical Gennext workflows for healthcare and research teams.',scope=['Germline interpretation','Somatic interpretation','Gennext workflows'],cta='Explore training',need='For professionals and teams developing their analysis skills.',delivery='Focused training on evaluating data, reviewing evidence and preparing findings for reporting.'),
 ],
 'tr':[
  dict(key='software',title='Yazılım',lead='Analiz, yorumlama ve raporlama.',body='Yazılım ürünümüz Gennext, klinik genomik ve longevity için veri işleme, değerlendirme ve raporlamayı bir araya getirir.',scope=['Gennext platformu','Klinik genomik','Longevity analizi ve raporlama'],cta='Yazılımı inceleyin',need='Karmaşık sağlık verileriyle çalışan ekipler için.',delivery='Analiz ve raporlamayı tek platformda buluşturan yazılım araçları ve otomatik iş akışları.'),
  dict(key='hardware',title='Donanım',lead='Hesaplama gücü, kurumunuzda.',body='Veri hacminize, analiz iş yükünüze ve mevcut ortamınıza göre yapılandırılan Worker Node ve sunucu altyapısı.',scope=['Worker Node','Yüksek hacimli sunucular','Yerel hesaplama ve depolama'],cta='Donanımı inceleyin',need='Kendi analiz kapasitesine ihtiyaç duyan kurumlar için.',delivery='Ekibinizin çalışma biçimine göre planlanan hesaplama ve depolama altyapısı.'),
  dict(key='training',title='Eğitim',lead='Analizin arkasındaki uzmanlığı geliştirin.',body='Sağlık ve araştırma ekiplerine yönelik genomik analiz, varyant yorumlama ve uygulamalı Gennext eğitimleri.',scope=['Germline varyant yorumlama','Somatik varyant yorumlama','Gennext iş akışları'],cta='Eğitimleri inceleyin',need='Analiz becerilerini geliştirmek isteyen profesyoneller ve ekipler için.',delivery='Veri değerlendirme, kanıt inceleme ve bulguları raporlamaya hazırlamaya odaklanan eğitimler.'),
 ]
}

def heading(eyebrow, title, description=''):
 return f'<div class="section-head"><div><p class="eyebrow">{eyebrow}</p><h2>{title}</h2></div>'+ (f'<p>{description}</p>' if description else '') + '</div>'

def hero(lang, page, title, description):
 d=CONTENT[lang]
 crumbs=f'<a href="index.html">{d["names"]["index"]}</a><span aria-hidden="true">/</span>'
 if page in ['software','hardware','training']:
  crumbs+=f'<a href="solutions.html">{d["names"]["solutions"]}</a><span aria-hidden="true">/</span>'
 crumbs+=f'<span aria-current="page">{d["names"][page]}</span>'
 return f'<section class="page-hero"><div class="container"><nav class="breadcrumb" aria-label="{t(lang,"Breadcrumb","Sayfa yolu")}">{crumbs}</nav><p class="eyebrow">{d["names"][page]}</p><h1>{title}</h1><p class="lead">{description}</p></div></section>'

def cta(lang, area=None):
 title=t(lang,'Let’s talk about your next step.','Bir sonraki adımı birlikte planlayalım.')
 desc=t(lang,'Tell us about your software, infrastructure or training needs.','Yazılım, altyapı veya eğitim ihtiyacınızı bizimle paylaşın.')
 label=t(lang,'Contact Geniva','Geniva ile iletişime geçin')
 if area:
  labels={'software':('Discuss your software needs','Yazılım ihtiyacınızı konuşalım'),'hardware':('Plan your infrastructure','Altyapınızı planlayalım'),'training':('Discuss training needs','Eğitim ihtiyacınızı konuşalım')}
  label=t(lang,*labels[area])
 return f'<section class="cta"><div class="container"><div><h2>{title}</h2><p>{desc}</p></div>{link(label,"contact.html"+("#"+area if area else ""),"button white")}</div></section>'

def training_visual(lang):
 rows=[('data',t(lang,'Review the data','Veriyi inceleyin')),('software',t(lang,'Evaluate the evidence','Kanıtları değerlendirin')),('report',t(lang,'Prepare findings for reporting','Bulguları raporlamaya hazırlayın'))]
 return '<div class="training-visual"><span class="visual-label">'+t(lang,'LEARN · APPLY · EVALUATE','ÖĞRENİN · UYGULAYIN · DEĞERLENDİRİN')+'</span>'+''.join(f'<div class="learning-step">{icon(k)}<span>{label}</span></div>' for k,label in rows)+'</div>'

def service_visual(key,lang,p):
 if key=='software':return '<div class="service-visual software-visual">'+image(p,'gennext-product.webp',t(lang,'Stylised Gennext analysis interface','Gennext analiz arayüzünün stilize gösterimi'),1672,941)+'</div>'
 if key=='hardware':return '<div class="service-visual hardware-visual">'+image(p,'hardware.jpg','Worker Node',1500,1500)+image(p,'server.webp',t(lang,'High-throughput server','Yüksek hacimli sunucu'),1254,1254)+'</div>'
 return training_visual(lang)

def service_cards(lang,p):
 cards=''
 for s in SERVICES[lang]:
  cards+=f'<article class="service-card"><div class="service-card-copy"><h3>{s["title"]}</h3><p class="service-lead">{s["lead"]}</p><p>{s["body"]}</p></div>{service_visual(s["key"],lang,p)}<ul class="service-scope">'+''.join(f'<li>{x}</li>' for x in s['scope'])+f'</ul>{link(s["cta"],s["key"]+".html")}</article>'
 return '<div class="services-grid">'+cards+'</div>'

def logo(name,p,data):
 info=data['logos'][name]
 return f'<span class="institution-logo">{image(p,info["asset"].removeprefix("assets/"),"",200,100)}</span><span class="institution-name">{esc(name)}</span>'

def evidence_teaser(lang,p,data):
 keys=[data['groups'][0][1][0], data['groups'][0][1][4], data['groups'][1][1][0], 'RootWell','Portakal Klinik','AlbertHealth']
 logos=''.join(f'<li>{logo(name,p,data)}</li>' for name in keys)
 return f'<section class="section evidence-section"><div class="container">{heading(t(lang,"REFERENCES & RESEARCH","REFERANSLAR VE ARAŞTIRMA"),t(lang,"Working with institutions.<br>Contributing to research.","Kurumlarla birlikte.<br>Bilimsel çalışmaların içinde."),t(lang,"Explore our clinical genomics and longevity references, and scientific studies using Gennext.","Klinik genomik ve longevity referanslarımızı, Gennext’in kullanıldığı bilimsel çalışmaları inceleyin."))}<ul class="logo-grid teaser-logos">{logos}</ul>{link(t(lang,"Explore references and publications","Referansları ve yayınları inceleyin"),"references.html")}</div></section>'

def home(lang,p,data):
 d=CONTENT[lang]
 title=t(lang,'Software, hardware and training for <span>health big data.</span>','Büyük sağlık verileri için <span>yazılım, donanım ve eğitim.</span>')
 intro=f'<section class="hero"><img class="hero-bg" src="{p}assets/hero.webp" width="1920" height="1080" alt="" fetchpriority="high"><div class="container hero-content"><p class="eyebrow">GENIVA</p><h1>{title}</h1><p class="hero-description">{d["subline"]}</p><div class="actions">{link(t(lang,"Explore our solutions","Çözümlerimizi inceleyin"),"solutions.html","button")}{link(t(lang,"Contact us","Bize ulaşın"),"contact.html","text-link light")}</div><p class="hero-audience">{t(lang,"For healthcare organisations, laboratories and research teams.","Sağlık kurumları, laboratuvarlar ve araştırma ekipleri için.")}</p></div></section>'
 services=f'<section class="section" id="solutions"><div class="container">{heading(t(lang,"WHAT WE DO","NE SUNUYORUZ"),t(lang,"Three areas of expertise.<br>One connected approach.","Üç uzmanlık alanı.<br>Bütünleşik bir yaklaşım."),t(lang,"Software to analyse. Infrastructure to compute. Training to put knowledge into practice.","Analiz için yazılım. Hesaplama için altyapı. Bilgiyi uygulamaya taşımak için eğitim."))}{service_cards(lang,p)}</div></section>'
 product=f'<section class="section product-band" id="gennext"><div class="container product-intro"><div>{image(p,"gennext.svg","Gennext",175,60,"product-logo")}<p class="eyebrow">{t(lang,"SOFTWARE BY GENIVA","GENIVA’NIN YAZILIM ÜRÜNÜ")}</p><h2>{t(lang,"Meet Gennext.","Gennext ile tanışın.")}</h2><p>{t(lang,"Our software platform for clinical genomics and longevity. Gennext connects data analysis, interpretation and reporting through automated workflows.","Klinik genomik ve longevity için geliştirdiğimiz yazılım platformu. Gennext, veri analizi, yorumlama ve raporlamayı otomatik iş akışlarıyla birleştirir.")}</p><div class="actions">{link(t(lang,"Explore our software solutions","Yazılım çözümlerimizi inceleyin"),"software.html")}{link(t(lang,"Visit gennext.bio","gennext.bio’yu ziyaret edin"),"https://gennext.bio",external=True)}</div></div><figure class="product-preview">{image(p,"gennext-product.webp",t(lang,"Stylised Gennext analysis screen","Gennext analiz ekranının stilize gösterimi"),1672,941)}<figcaption>{t(lang,"A stylised view of the Gennext interface.","Gennext arayüzünün stilize gösterimi.")}</figcaption></figure></div></section>'
 applications=f'<section class="section"><div class="container">{heading(t(lang,"APPLICATION AREAS","UYGULAMA ALANLARI"),t(lang,"Technology grounded in<br>health and life sciences.","Sağlık ve yaşam bilimlerinden<br>güç alan teknoloji."))}<div class="application-grid"><article><p class="eyebrow">CLINICAL GENOMICS</p><h3>{t(lang,"From sequencing data to reporting.","Dizileme verisinden raporlamaya.")}</h3><p>{t(lang,"Somatic and germline analysis, with short-read and long-read workflows for clinical and research applications.","Klinik ve araştırma uygulamalarında short-read ve long-read iş akışlarıyla somatik ve germline analiz.")}</p>{link(t(lang,"Explore clinical genomics","Klinik genomiği inceleyin"),"software.html#clinical")}</article><article><p class="eyebrow">LONGEVITY</p><h3>{t(lang,"Automated analysis and reporting.","Otomatik analiz ve raporlama.")}</h3><p>{t(lang,"Genetic and epigenetic assessment through Gennext, supported by our laboratory and wider multi-omics approach.","Laboratuvarımız ve multiomik yaklaşımımızla desteklenen, Gennext üzerinden genetik ve epigenetik değerlendirme.")}</p>{link(t(lang,"Explore longevity solutions","Longevity çözümlerini inceleyin"),"software.html#longevity")}</article></div></div></section>'
 return intro+services+product+applications+evidence_teaser(lang,p,data)+cta(lang)

def solutions(lang,p):
 intro=hero(lang,'solutions',t(lang,'Software. Hardware. Training.','Yazılım. Donanım. Eğitim.'),t(lang,'Three complementary areas of expertise for health data analysis, interpretation and reporting. Choose the support your team needs.','Sağlık verilerinin analizi, yorumlanması ve raporlanması için birbirini tamamlayan üç uzmanlık alanı. Ekibinizin ihtiyaç duyduğu çözümü seçin.'))
 rows=''
 for s in SERVICES[lang]:
  rows+=f'<article class="solution-row" id="{s["key"]}"><div class="solution-copy"><p class="eyebrow">GENIVA / {s["title"]}</p><h2>{s["title"]}</h2><p class="solution-lead">{s["lead"]}</p><p>{s["body"]}</p><dl class="offer-details"><div><dt>{t(lang,"Who it’s for","Kimler için")}</dt><dd>{s["need"]}</dd></div><div><dt>{t(lang,"What we provide","Ne sunuyoruz")}</dt><dd>{s["delivery"]}</dd></div></dl>{link(s["cta"],s["key"]+".html","button navy")}</div><div class="solution-art">{service_visual(s["key"],lang,p)}<ul class="service-scope">'+''.join(f'<li>{x}</li>' for x in s['scope'])+'</ul></div></article>'
 return intro+f'<section class="section solution-overview"><div class="container">{rows}</div></section>'+cta(lang)

def video(lang):
 return f'<section class="section video-section" id="community"><div class="container">{heading("GENNEXT",t(lang,"See the platform in action.","Platformu yakından tanıyın."),t(lang,"Watch our introduction, then explore Gennext Community for tutorials and analysis workflows.","Tanıtım videomuzu izleyin; kullanım eğitimleri ve analiz iş akışları için Gennext Community kanalını ziyaret edin."))}<div class="intro-video"><iframe src="https://www.youtube-nocookie.com/embed/bQ-PGMYtemI" title="{t(lang,"Gennext introduction video","Gennext tanıtım videosu")}" width="1120" height="630" loading="lazy" referrerpolicy="strict-origin-when-cross-origin" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe></div><div class="video-links">{link(t(lang,"Watch on YouTube","YouTube’da izleyin"),"https://www.youtube.com/watch?v=bQ-PGMYtemI",external=True)}{link(t(lang,"Explore video tutorials","Video eğitimlerini inceleyin"),CHANNEL,external=True)}</div></div></section>'

def laboratory(lang,p):
 return f'<div class="lab-support" id="laboratory"><figure>{image(p,"laboratory.jpg",t(lang,"Geniva laboratory workspace","Geniva laboratuvarı çalışma alanı"),600,338)}</figure><div><p class="eyebrow">{t(lang,"LABORATORY SUPPORT","LABORATUVAR DESTEĞİ")}</p><h3>{t(lang,"Our laboratory, supporting longevity.","Longevity çalışmalarını destekleyen laboratuvarımız.")}</h3><p>{t(lang,"Our laboratory work complements Gennext’s analysis and reporting workflows.","Laboratuvar çalışmalarımız, Gennext’in analiz ve raporlama iş akışlarını tamamlar.")}</p><dl class="lab-capabilities"><div><dt>Microarray</dt><dd>{t(lang,"Genotyping and DNA methylation workflows for genetic and epigenetic assessment.","Genetik ve epigenetik değerlendirme için genotipleme ve DNA metilasyonu çalışmaları.")}</dd></div><div><dt>{t(lang,"Long-read sequencing","Long-read dizileme")}</dt><dd>{t(lang,"Nanopore sequencing and analysis aligned with the aims of each study.","Çalışmanın amacına uygun Nanopore dizileme ve analiz.")}</dd></div></dl></div></div>'

def software(lang,p):
 intro=hero(lang,'software',t(lang,'Software for health data<br>analysis and reporting.','Sağlık verileri için<br>analiz ve raporlama yazılımı.'),t(lang,'We develop software that connects data processing, interpretation and reporting. Gennext is Geniva’s platform for clinical genomics and longevity.','Veri işleme, yorumlama ve raporlamayı bir araya getiren yazılımlar geliştiriyoruz. Gennext, Geniva’nın klinik genomik ve longevity platformudur.'))
 product=f'<section class="section" id="gennext"><div class="container">{heading(t(lang,"SOFTWARE BY GENIVA","GENIVA’NIN YAZILIM ÜRÜNÜ"),"Gennext",t(lang,"A shared workspace for analysis, evidence review and reporting. Explore the product on gennext.bio or talk to us about your workflow.","Analiz, kanıt inceleme ve raporlama için ortak bir çalışma alanı. Ürünü gennext.bio üzerinden inceleyin veya iş akışınızı bizimle konuşun."))}<div class="actions">{contact_link(t(lang,"Discuss your software needs","Yazılım ihtiyacınızı konuşalım"),"software","button navy")}{link(t(lang,"Explore Gennext","Gennext’i keşfedin"),"https://gennext.bio",external=True)}</div><figure class="product-illustration">{image(p,"gennext-product.webp",t(lang,"Stylised Gennext screen with quality control, filters and variant evaluation","Kalite kontrol, filtreler ve varyant değerlendirme içeren stilize Gennext ekranı"),1672,941)}<figcaption>{t(lang,"A stylised view of the Gennext interface.","Gennext arayüzünün stilize gösterimi.")}</figcaption></figure><nav class="section-nav" aria-label="{t(lang,"Software application areas","Yazılım uygulama alanları")}"><a href="#clinical">Clinical Genomics</a><a href="#longevity">Longevity</a><a href="#laboratory">{t(lang,"Laboratory support","Laboratuvar desteği")}</a></nav></div></section>'
 clinical=f'<section class="section cream" id="clinical"><div class="container">{heading("GENNEXT CLINICAL",t(lang,"Clinical genomics.<br>From data to evaluation.","Klinik genomik.<br>Veriden değerlendirmeye."),t(lang,"Tools and workflows for processing sequencing data, assessing variants and preparing findings for reporting in clinical and research settings.","Klinik ve araştırma çalışmalarında dizileme verilerini işlemek, varyantları değerlendirmek ve bulguları raporlamaya hazırlamak için araçlar ve iş akışları."))}<div class="application-grid"><article><p class="eyebrow">{t(lang,"SOMATIC","SOMATİK")}</p><h3>{t(lang,"Oncology and molecular pathology","Onkoloji ve moleküler patoloji")}</h3><p>{t(lang,"Assessment of variants, fusions and biomarkers from tumour sequencing data, with reporting that supports specialist review.","Tümör dizileme verilerinden varyant, füzyon ve biyobelirteç bulgularının değerlendirilmesi; uzman incelemesini destekleyen raporlama.")}</p></article><article><p class="eyebrow">GERMLINE</p><h3>{t(lang,"Inherited conditions and rare diseases","Kalıtsal hastalıklar ve nadir hastalıklar")}</h3><p>{t(lang,"Variant filtering, prioritisation and evidence review in the context of genetic findings, family information and phenotype.","Genetik bulgular, aile bilgisi ve fenotip bağlamında varyant filtreleme, önceliklendirme ve kanıt inceleme.")}</p></article></div><div class="sequencing-options"><article><h3>Short-read</h3><p>{t(lang,"Processing and assessment of panel, exome and whole-genome sequencing data.","Panel, ekzom ve tüm genom dizileme verilerinin işlenmesi ve değerlendirilmesi.")}</p></article><article><h3>Long-read</h3><p>{t(lang,"Long-read data analysis planned around the data type and research question.","Veri türüne ve araştırma sorusuna göre planlanan uzun okuma veri analizi.")}</p></article></div></div></section>'
 workflow=[('data',t(lang,'Genetic & epigenetic data','Genetik ve epigenetik veri')),('software',t(lang,'Automated analysis','Otomatik analiz')),('report',t(lang,'Reporting','Raporlama'))]
 flow='<ol class="workflow">'+''.join(f'<li>{icon(key)}<strong>{label}</strong></li>' for key,label in workflow)+'</ol>'
 longevity=f'<section class="section" id="longevity"><div class="container">{heading("GENNEXT LONGEVITY",t(lang,"Automated analysis.<br>Reporting through Gennext.","Otomatik analiz.<br>Gennext üzerinden raporlama."),t(lang,"We bring genetic and epigenetic assessment into longevity services. Analysis and report generation run through Gennext, supporting healthcare professionals and organisations.","Genetik ve epigenetik değerlendirmeyi longevity hizmetleriyle birleştiriyoruz. Analiz ve rapor üretimi, sağlık profesyonellerini ve kurumları desteklemek üzere Gennext üzerinden otomatik yürütülür."))}{flow}<div class="longevity-context"><h3>{t(lang,"A broader biological context","Daha geniş bir biyolojik bağlam")}</h3><p>{t(lang,"Our multi-omics approach considers genomic, transcriptomic, epigenetic, metabolomic and lipidomic data together. Genetic predisposition and epigenetic assessments support personalised health and wellness services.","Multiomik yaklaşımımız genomik, transkriptomik, epigenetik, metabolomik ve lipidomik verileri birlikte ele alır. Genetik yatkınlık ve epigenetik değerlendirmeler, kişiselleştirilmiş sağlık ve sağlıklı yaşam hizmetlerini destekler.")}</p></div><p class="scope-note">{t(lang,"Longevity reports support personalised health guidance; they are not diagnostic tests.","Longevity raporları kişiselleştirilmiş sağlık danışmanlığını destekler; tanı testi değildir.")}</p>{laboratory(lang,p)}{contact_link(t(lang,"Discuss longevity analysis and reporting","Longevity analizi ve raporlamayı konuşalım"),"software","text-link")}</div></section>'
 return intro+product+clinical+longevity+video(lang)+cta(lang,'software')

def hardware_gallery(lang,p):
 items=[('hardware.jpg','Worker Node',t(lang,'On-site analysis workstation','Kurum içi analiz istasyonu')),('server.webp',t(lang,'High-throughput server','Yüksek hacimli sunucu'),t(lang,'For intensive and concurrent analysis workloads','Yoğun ve eş zamanlı analiz iş yükleri için'))]
 return '<div class="hardware-gallery">'+''.join(f'<figure><div class="hardware-image">{image(p,file,title,1500 if file.endswith("jpg") else 1254,1500 if file.endswith("jpg") else 1254)}</div><figcaption><h3>{title}</h3><p>{desc}</p></figcaption></figure>' for file,title,desc in items)+'</div>'

def federation(lang):
 nodes=''
 for letter in 'ABC':
  labels=[('data',t(lang,'Genomic data','Genomik veri')),('hardware','Worker Node'),('report',t(lang,'Analysis output','Analiz çıktısı'))]
  pipeline='<div class="local-pipeline">'+ '<span class="flow-arrow" aria-hidden="true">→</span>'.join(f'<div>{icon(k)}<strong>{label}</strong></div>' for k,label in labels)+'</div>'
  nodes+=f'<article class="federation-node"><h3>{t(lang,"Institution","Kurum")} {letter}</h3><p class="local-label">{t(lang,"LOCAL INFRASTRUCTURE","YEREL ALTYAPI")}</p>{pipeline}<p class="local-retention">{icon("lock")}<span>{t(lang,"Data and computing stay on site","Veri ve hesaplama kurumda kalır")}</span></p></article>'
 return f'<figure class="federation-visual"><div class="federation-heading"><span>GENNEXT</span><strong>{t(lang,"One platform. Distributed analysis.","Tek platform. Dağıtık analiz gücü.")}</strong></div><div class="federation-coordinator">{icon("software")}<div><h3>{t(lang,"Central coordination","Merkezi koordinasyon")}</h3><p>{t(lang,"User access · Task assignment · Workflow status","Kullanıcı erişimi · Görev atama · İşlem durumu")}</p></div></div><div class="coordination-lane"><span aria-hidden="true">↓ ↑</span><p>{t(lang,"Analysis tasks and status information","Analiz görevi ve durum bilgisi")}</p></div><div class="federation-nodes">{nodes}</div><figcaption><span class="legend-local"></span>{t(lang,"Genomic inputs and analysis outputs are processed locally.","Genomik girdiler ve analiz çıktıları yerelde işlenir.")}<br><span class="legend-control"></span>{t(lang,"Access, task and workflow metadata required for coordination are shared with central services.","Koordinasyon için gerekli erişim, görev ve süreç üst verileri merkezi hizmetlerle paylaşılır.")}</figcaption></figure>'

def hardware(lang,p):
 intro=hero(lang,'hardware',t(lang,'Computing infrastructure.<br>Built around your workload.','Hesaplama altyapısı.<br>İş yükünüze göre planlanır.'),t(lang,'We provide on-site computing and storage infrastructure for health data analysis. Capacity is planned around data volumes, concurrent workloads and your existing environment.','Sağlık verilerinin analizi için kurum içi hesaplama ve depolama altyapısı sunuyoruz. Kapasiteyi veri hacmi, eş zamanlı iş yükü ve mevcut ortamınıza göre planlıyoruz.'))
 machines=f'<section class="section" id="hardware"><div class="container">{heading(t(lang,"ON-SITE COMPUTING","KURUM İÇİ HESAPLAMA"),t(lang,"The right capacity<br>for your team.","Ekibiniz için<br>uygun kapasite."),t(lang,"From a local Worker Node to a higher-capacity server, we consider computing, memory and storage together.","Yerel Worker Node’dan daha yüksek kapasiteli sunucuya kadar hesaplama, bellek ve depolama kaynaklarını birlikte ele alıyoruz."))}{hardware_gallery(lang,p)}</div></section>'
 plans=t(lang,[('Data volume','The type and volume of data you process, and your storage needs.'),('Analysis workload','The analyses you run and how many need to run at the same time.'),('Existing environment','Your current infrastructure and the way your team works.')],[('Veri hacmi','İşlediğiniz verinin türü ve hacmi ile depolama ihtiyacınız.'),('Analiz iş yükü','Yürüttüğünüz analizler ve aynı anda çalışması gereken işlem sayısı.'),('Mevcut ortam','Kurumunuzun altyapısı ve ekibinizin çalışma biçimi.')])
 planning=f'<section class="section cream"><div class="container">{heading(t(lang,"CAPACITY PLANNING","KAPASİTE PLANLAMA"),t(lang,"Start with the work<br>you need to do.","İşe ihtiyacınız olan<br>kapasiteyi belirleyerek başlayın."))}<div class="detail-grid">'+''.join(f'<article><h3>{a}</h3><p>{b}</p></article>' for a,b in plans)+f'</div>{contact_link(t(lang,"Plan your infrastructure","Altyapınızı planlayalım"),"hardware","button navy")}</div></section>'
 arch=f'<section class="section" id="federation"><div class="container">{heading(t(lang,"FEDERATED ARCHITECTURE","FEDERE MİMARİ"),t(lang,"Local processing.<br>Central coordination.","Yerel işleme.<br>Merkezi koordinasyon."),t(lang,"In Gennext’s federated workflow, genomic data is processed on the assigned local infrastructure. Central services coordinate access and analysis tasks.","Gennext’in federe iş akışında genomik veriler atanmış yerel altyapıda işlenir. Merkezi hizmetler erişimi ve analiz görevlerini koordine eder."))}{federation(lang)}<div class="actions">{link(t(lang,"Explore Gennext software","Gennext yazılımını inceleyin"),"software.html")}{link(t(lang,"Visit gennext.bio","gennext.bio’yu ziyaret edin"),"https://gennext.bio",external=True)}</div></div></section>'
 return intro+machines+planning+arch+cta(lang,'hardware')

def training(lang,p):
 intro=hero(lang,'training',t(lang,'Training that connects<br>knowledge and practice.','Bilgiyi uygulamayla<br>buluşturan eğitimler.'),t(lang,'Develop skills in genomic data analysis, variant interpretation and Gennext workflows. Our training brings scientific context and practical evaluation together.','Genomik veri analizi, varyant yorumlama ve Gennext iş akışlarında yetkinliğinizi geliştirin. Eğitimlerimiz bilimsel bağlam ile uygulamalı değerlendirmeyi bir araya getirir.'))
 audience=f'<section class="section"><div class="container training-intro"><div><p class="eyebrow">{t(lang,"WHO IT’S FOR","KİMLER İÇİN")}</p><h2>{t(lang,"For the people<br>behind the analysis.","Analizi yürüten<br>profesyoneller için.")}</h2><p>{t(lang,"Healthcare professionals, laboratory teams and researchers working with genomic data. We discuss your team’s background and objectives to define the training scope.","Genomik verilerle çalışan sağlık profesyonelleri, laboratuvar ekipleri ve araştırmacılar. Eğitim kapsamını belirlemek için ekibinizin deneyimini ve hedeflerini birlikte değerlendiriyoruz.")}</p>{contact_link(t(lang,"Discuss training needs","Eğitim ihtiyacınızı konuşalım"),"training","button navy")}</div>{training_visual(lang)}</div></section>'
 topics=t(lang,[('Germline variants','Inherited conditions and rare diseases',['Evaluate variants alongside phenotypes and family information.','Review evidence and approaches to variant prioritisation.']),('Somatic variants','Oncology and molecular pathology',['Filter and assess genomic findings in tumour data.','Review supporting evidence and prepare findings for reporting.']),('Gennext workflows','From analysis to reporting',['Navigate the platform and review analysis outputs.','Use filtering, evaluation and reporting tools in a connected workflow.'])],[('Germline varyantlar','Kalıtsal ve nadir hastalıklar',['Varyantları fenotip ve aile bilgisiyle birlikte değerlendirin.','Kanıtları ve varyant önceliklendirme yaklaşımlarını inceleyin.']),('Somatik varyantlar','Onkoloji ve moleküler patoloji',['Tümör verilerindeki genomik bulguları filtreleyin ve değerlendirin.','Destekleyici kanıtları inceleyip bulguları raporlamaya hazırlayın.']),('Gennext iş akışları','Analizden raporlamaya',['Platformu kullanın ve analiz çıktılarını inceleyin.','Filtreleme, değerlendirme ve raporlama araçlarını aynı iş akışında kullanın.'])])
 topic_html=''.join(f'<article><h3>{name}</h3><p class="topic-context">{context}</p><ul>'+''.join(f'<li>{x}</li>' for x in outcomes)+'</ul></article>' for name,context,outcomes in topics)
 scope=f'<section class="section cream" id="training"><div class="container">{heading(t(lang,"TRAINING SCOPE","EĞİTİM KAPSAMI"),t(lang,"What your team<br>can put into practice.","Ekibinizin uygulamaya<br>taşıyabileceği beceriler."))}<div class="detail-grid training-topics">{topic_html}</div></div></section>'
 resources=f'<section class="section"><div class="container resource-band"><div><p class="eyebrow">GENNEXT COMMUNITY</p><h2>{t(lang,"Keep learning<br>with video tutorials.","Video eğitimleriyle<br>öğrenmeye devam edin.")}</h2><p>{t(lang,"Explore platform tutorials and analysis workflows on our YouTube channel. For a team training programme, contact us to discuss scope and participation.","YouTube kanalımızda platform kullanım eğitimlerini ve analiz iş akışlarını inceleyin. Ekip eğitimleri için kapsam ve katılım bilgilerini bizimle konuşun.")}</p></div><div class="resource-links">{link(t(lang,"Explore video tutorials","Video eğitimlerini inceleyin"),CHANNEL,"button navy",True)}{link(t(lang,"Watch the Gennext introduction","Gennext tanıtımını izleyin"),"software.html#community")}</div></div></section>'
 return intro+audience+scope+resources+cta(lang,'training')

def about(lang,p,data):
 intro=hero(lang,'about',t(lang,'Health data.<br>Scientific expertise.<br>Practical technology.','Sağlık verileri.<br>Bilimsel uzmanlık.<br>Uygulamaya dönük teknoloji.'),t(lang,'Geniva develops software, builds computing infrastructure and provides training for health data analysis, interpretation and reporting.','Geniva, sağlık verilerinin analizi, yorumlanması ve raporlanması için yazılım geliştirir, hesaplama altyapısı kurar ve eğitim verir.'))
 company=f'<section class="section"><div class="container about-intro"><h2>{t(lang,"Three areas of expertise.<br>A shared purpose.","Üç uzmanlık alanı.<br>Ortak bir amaç.")}</h2><div><p>{t(lang,"Geniva Bilişim Sağlık A.Ş. brings software, hardware and training together to support healthcare organisations, laboratories and research teams working with complex health data.","Geniva Bilişim Sağlık A.Ş., karmaşık sağlık verileriyle çalışan sağlık kurumlarını, laboratuvarları ve araştırma ekiplerini desteklemek için yazılım, donanım ve eğitimi bir araya getirir.")}</p><p>{t(lang,"Gennext is our software product for clinical genomics and longevity. Our computing infrastructure and training complement the platform, helping teams connect data processing with evaluation and reporting.","Gennext, klinik genomik ve longevity için geliştirdiğimiz yazılım ürünüdür. Hesaplama altyapımız ve eğitimlerimiz, veri işlemeyi değerlendirme ve raporlamayla buluşturmak üzere platformu tamamlar.")}</p>{link(t(lang,"Explore our solutions","Çözümlerimizi inceleyin"),"solutions.html")}</div></div></section>'
 omics=t(lang,[('Genomics','DNA variation'),('Transcriptomics','RNA expression'),('Epigenomics','Epigenetic patterns'),('Metabolomics','Metabolic processes'),('Lipidomics','Lipid composition')],[('Genomik','DNA varyasyonları'),('Transkriptomik','RNA ekspresyonu'),('Epigenomik','Epigenetik örüntüler'),('Metabolomik','Metabolik süreçler'),('Lipidomik','Lipit bileşimi')])
 scientific=f'<section class="section cream"><div class="container">{heading(t(lang,"OUR SCIENTIFIC APPROACH","BİLİMSEL YAKLAŞIMIMIZ"),t(lang,"Considering the layers<br>of biology together.","Biyolojinin farklı<br>katmanlarını birlikte ele alıyoruz."),t(lang,"Our multi-omics approach considers genomic, transcriptomic, epigenetic, metabolomic and lipidomic data in a shared biological context, around the question each study seeks to answer.","Multiomik yaklaşımımız; genomik, transkriptomik, epigenetik, metabolomik ve lipidomik verileri, çalışmanın yanıt aradığı soru etrafında ortak bir biyolojik bağlamda değerlendirmeye dayanır."))}<div class="omics-layers">'+''.join(f'<article><h3>{name}</h3><p>{desc}</p></article>' for name,desc in omics)+'</div></div></section>'
 lab=f'<section class="section"><div class="container about-intro"><div><p class="eyebrow">{t(lang,"LABORATORY CAPABILITY","LABORATUVAR KAPASİTEMİZ")}</p><h2>{t(lang,"Laboratory work<br>that supports our solutions.","Çözümlerimizi destekleyen<br>laboratuvar çalışmaları.")}</h2></div><div><p>{t(lang,"Our own laboratory carries out microarray genotyping, DNA methylation work and Nanopore long-read sequencing. This capacity supports our longevity analysis and reporting workflows.","Kendi laboratuvarımızda microarray genotipleme, DNA metilasyonu ve Nanopore uzun okuma dizileme çalışmaları yürütüyoruz. Bu kapasite, longevity analiz ve raporlama iş akışlarımızı destekler.")}</p>{link(t(lang,"Explore laboratory support","Laboratuvar desteğini inceleyin"),"software.html#laboratory")}</div></div></section>'
 return intro+company+scientific+lab+evidence_teaser(lang,p,data)+cta(lang)

def references(lang,p,data):
 intro=hero(lang,'references',t(lang,'Working with institutions.<br>Contributing to research.','Kurumlarla birlikte.<br>Bilimsel çalışmaların içinde.'),t(lang,'Our references across clinical genomics and longevity, followed by selected scientific publications using Gennext.','Klinik genomik ve longevity alanlarındaki referanslarımız ile Gennext’in kullanıldığı bilimsel yayınlardan seçkiler.'))
 groups=''
 for name,names in data['groups']:
  name=t(lang,'Somatic','Somatik') if name=='Somatik / Somatic' else name
  groups+=f'<article class="reference-group"><h3>{name}</h3><ul class="logo-grid">'+''.join(f'<li>{logo(n,p,data)}</li>' for n in names)+'</ul></article>'
 refs=f'<section class="section"><div class="container">{heading(t(lang,"OUR REFERENCES","REFERANSLARIMIZ"),t(lang,"Shared work.<br>Different areas of practice.","Ortak çalışmalar.<br>Farklı uygulama alanları."))}<div class="reference-groups">{groups}</div></div></section>'
 citations=''
 for url,c in data['citations'].items():
  label='doi: '+c['doi'] if c['doi'] else t(lang,'View publication','Yayını görüntüle')
  citations+=f'<li class="citation"><p>{esc(c["authors"])} {esc(c["title"])}. <i>{esc(c["journal"])}</i> {esc(c["details"])}</p>{link(label,url,external=True)}</li>'
 pubs=f'<section class="section cream" id="publications"><div class="container">{heading(t(lang,"SCIENTIFIC PUBLICATIONS","BİLİMSEL YAYINLAR"),t(lang,"Gennext in research","Araştırmalarda Gennext"),t(lang,"Selected studies using Gennext. Publication details and original sources are provided below.","Gennext’in kullanıldığı bilimsel çalışmalardan seçkiler. Yayın künyeleri ve özgün kaynak bağlantıları aşağıda yer alıyor."))}<ol class="citation-list">{citations}</ol></div></section>'
 return intro+refs+pubs+cta(lang)

def contact(lang,p,address,maps):
 intro=hero(lang,'contact',t(lang,'Let’s talk about<br>your needs.','İhtiyacınızı<br>konuşalım.'),t(lang,'Tell us what you want to analyse, the infrastructure you need or the skills your team wants to develop.','Analiz etmek istediğiniz verileri, ihtiyaç duyduğunuz altyapıyı veya ekibinizin geliştirmek istediği becerileri bizimle paylaşın.'))
 options=t(lang,[('software','Software & Reporting','Discuss Gennext, clinical genomics or longevity analysis and reporting, including laboratory support.','Geniva software and reporting enquiry'),('hardware','Hardware & Infrastructure','Discuss your data volumes, analysis capacity and on-site computing needs.','Geniva infrastructure enquiry'),('training','Training','Tell us about your team and the analysis or interpretation skills you want to develop.','Geniva training enquiry')],[('software','Yazılım ve Raporlama','Gennext, klinik genomik veya laboratuvar desteği dahil longevity analizi ve raporlamayı konuşalım.','Geniva yazılım ve raporlama görüşmesi'),('hardware','Donanım ve Altyapı','Veri hacminizi, analiz kapasitenizi ve kurum içi hesaplama ihtiyacınızı konuşalım.','Geniva altyapı görüşmesi'),('training','Eğitim','Ekibinizi ve geliştirmek istediğiniz analiz veya yorumlama becerilerini bize anlatın.','Geniva eğitim görüşmesi')])
 cards=''.join(f'<a class="contact-option" id="{key}" href="mailto:info@gennext.bio?subject={quote(subject)}"><div>{icon(key)}<h3>{title}</h3>{ARROW}</div><p>{desc}</p></a>' for key,title,desc,subject in options)
 email=t(lang,'Email','E-posta');phone=t(lang,'Phone','Telefon')
 contactinfo=f'<section class="section"><div class="container contact-grid"><div class="contact-info"><p class="eyebrow">GENIVA</p><h2>{t(lang,"Start a conversation.","İletişime geçin.")}</h2><p>{t(lang,"Share a short description of your organisation and the support you need.","Kurumunuzu ve ihtiyaç duyduğunuz desteği kısaca paylaşabilirsiniz.")}</p><div class="contact-method"><span>{email}</span><a href="mailto:info@gennext.bio">info@gennext.bio</a><button class="copy-email" type="button">{t(lang,"Copy email address","E-posta adresini kopyala")}</button><p class="copy-status" role="status" aria-live="polite"></p></div><div class="contact-method"><span>{phone}</span><a href="tel:+902162504471">+90 216 250 4471</a></div></div><div class="contact-options">{cards}<p class="contact-note">{t(lang,"Choose a topic to open a message in your email application.","Bir başlık seçtiğinizde e-posta uygulamanızda ilgili konuyla yeni bir ileti açılır.")}</p></div></div><div class="container"><div class="location-card"><div><p class="eyebrow">{t(lang,"FIND US","ADRESİMİZ")}</p><h2>Acıbadem Üniversitesi TEKMER</h2></div><div><address>{address}</address>{link(t(lang,"Get directions","Yol tarifi alın"),maps,external=True)}</div></div></div></section>'
 return intro+contactinfo

def render_page(page,lang,p,data,address,maps):
 if page in ['index','about','references']:
  return {'index':home,'about':about,'references':references}[page](lang,p,data)
 if page=='contact':return contact(lang,p,address,maps)
 return {'solutions':solutions,'software':software,'hardware':hardware,'training':training}[page](lang,p)
