"""Bilingual contact form. Submissions are handled by the site's Worker."""
from html import escape

CONSENT = {
 'en': 'I would like to receive marketing emails from Geniva about products, events and education.',
 'tr': 'Geniva’dan ürünler, etkinlikler ve eğitimler hakkında pazarlama e-postaları almak istiyorum.',
}

def form(lang):
 def t(en,tr):return tr if lang=='tr' else en
 topics=[('general',t('General enquiry','Genel görüşme')),('demo',t('Gennext demo','Gennext demosu')),('software',t('Software & Reporting','Yazılım ve Raporlama')),('hardware',t('Hardware & Infrastructure','Donanım ve Altyapı')),('training',t('Education','Eğitim')),('career',t('Career application','Kariyer başvurusu'))]
 options=''.join(f'<option value="{key}">{label}</option>' for key,label in topics)
 return f'''<div class="callback-panel" id="message">
 <span id="demo" class="section-anchor"></span><span id="career" class="section-anchor"></span>
 <p class="eyebrow">{t('LET’S CONNECT','TANIŞALIM')}</p>
 <h2 data-form-heading>{t('Send a message.<br>Let’s talk.','Bize yazın.<br>Görüşelim.')}</h2>
 <p class="callback-description">{t('Send your message here. Prefer a callback? Choose phone below and tell us when to reach you.','Mesajınızı buradan gönderin. Sizi aramamızı isterseniz aşağıdan telefonu seçip uygun olduğunuz zamanı belirtin.')}</p>
 <form id="contact-form" action="/api/contact" method="post" aria-label="{t('Contact Geniva','Geniva iletişim formu')}">
 <p class="form-help">{t('Fields marked * are required.','* işaretli alanlar zorunludur.')}</p>
 <div class="field"><label for="contact-topic">{t('What can we help with?','Hangi konuda görüşelim?')} *</label><select id="contact-topic" name="topic" required>{options}</select></div>
 <div class="form-row"><div class="field"><label for="contact-name">{t('Your name','Adınız soyadınız')} *</label><input id="contact-name" name="name" autocomplete="name" required maxlength="120"></div><div class="field"><label for="contact-email">{t('Email address','E-posta adresiniz')} *</label><input id="contact-email" name="email" type="email" autocomplete="email" required maxlength="254"></div></div>
 <div class="field"><label for="contact-organization">{t('Organisation (optional)','Kurum (isteğe bağlı)')}</label><input id="contact-organization" name="organization" autocomplete="organization" maxlength="160"></div>
 <fieldset class="reply-choice"><legend>{t('How would you like us to reply?','Size nasıl ulaşalım?')}</legend><label><input type="radio" name="reply_by" value="email" checked>{t('By email','E-posta ile')}</label><label><input type="radio" name="reply_by" value="phone">{t('Call me back','Beni arayın')}</label></fieldset>
 <div class="form-row"><div class="field"><label for="contact-phone">{t('Phone','Telefon')} <span data-phone-optional>{t('(optional)','(isteğe bağlı)')}</span><span data-phone-required hidden>*</span></label><input id="contact-phone" name="phone" type="tel" autocomplete="tel" maxlength="40" placeholder="+90 ..."></div><div class="field"><label for="contact-time">{t('Preferred time (optional)','Uygun gün / saat (isteğe bağlı)')}</label><input id="contact-time" name="preferred_time" maxlength="160" placeholder="{t('Day, time and time zone','Gün, saat ve saat dilimi')}"></div></div>
 <div class="field" data-career-field hidden><label for="contact-portfolio">{t('CV, LinkedIn or portfolio link (optional)','CV, LinkedIn veya portfolyo bağlantısı (isteğe bağlı)')}</label><input id="contact-portfolio" name="portfolio_url" type="url" maxlength="1000" placeholder="https://" disabled></div>
 <div class="field"><label for="contact-message">{t('Your message','Mesajınız')} *</label><textarea id="contact-message" name="message" rows="4" required minlength="10" maxlength="4000" placeholder="{t('A few words about your needs, team or project.','İhtiyacınız, ekibiniz veya projeniz hakkında birkaç cümle.')}" aria-describedby="message-help"></textarea><p id="message-help" class="field-help">{t('Please don’t include patient details or sensitive health information.','Lütfen hasta bilgisi veya hassas sağlık verisi paylaşmayın.')}</p></div>
 <div class="form-trap" aria-hidden="true"><label for="contact-website">Website</label><input id="contact-website" name="website" tabindex="-1" autocomplete="off"></div>
 <label class="marketing-choice"><input type="checkbox" name="marketing_opt_in" value="yes"><span>{CONSENT[lang]} <small>{t('Optional. You can change your preference by emailing info@gennext.bio.','İsteğe bağlıdır. Tercihinizi değiştirmek için info@gennext.bio adresine yazabilirsiniz.')}</small></span></label>
 <p class="form-privacy">{t('Geniva Bilişim Sağlık A.Ş. uses your details to handle your enquiry or application and reply to you. Marketing permission is separate and is not required to send this form. For questions about your data or deletion requests:','Geniva Bilişim Sağlık A.Ş., bilgilerinizi talebinizi veya başvurunuzu değerlendirmek ve size yanıt vermek için kullanır. Pazarlama izni ayrıdır; formu göndermek için gerekli değildir. Verilerinizle ilgili sorularınız veya silme talepleriniz için:')} <a href="mailto:info@gennext.bio">info@gennext.bio</a>.</p>
 <button class="button form-submit" type="submit" disabled>{t('Send message','Mesajı gönder')} <span aria-hidden="true">→</span></button>
 <p class="form-status" role="status" aria-live="polite" tabindex="-1"></p>
 <noscript><p class="form-help">{t('Sending this form needs JavaScript. You can also email info@gennext.bio or call +90 216 250 4471.','Bu formu göndermek için JavaScript gerekir. info@gennext.bio adresine yazabilir veya +90 216 250 4471 numarasını arayabilirsiniz.')}</p></noscript>
 </form></div>'''
