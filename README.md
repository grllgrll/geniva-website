# Geniva website

English-first corporate site centred on **Software, Hardware and Education for health big data**. Turkish pages are under `/tr/`; `/en/` keeps old links working. Education retains `training.html` for compatibility. Specific programmes and practical learning still use “training”.

## Source and build

- `site_pages.py`: bilingual content and page templates.
- `contact_form.py`: form, field labels, exact marketing consent text.
- `build.py`: header/footer, routes and metadata; 18 pages and 9 redirects.
- `styles.css`, `app.js`: responsive layout, navigation, topic selection and form submission.
- `worker/index.mjs`: contact API and authenticated inbox; `worker/inbox.html`: inbox UI.
- `db/schema.ts`, `drizzle/`: schema and immutable generated migrations.
- `assets/reference-data.json`: approved reference groups, logos and full citations.

Run `npm ci` to install migration tooling, then `npm run build`. The existing Python build generates static assets in `dist/client`, a Worker in `dist/server/index.js` and migration metadata in `dist/.openai`. The hosting manifest declares D1 binding `DB`; Sites provisions it and applies the migrations. The Worker delegates public pages and assets to `ASSETS`.

After schema edits use `npm run db:generate`. Never alter applied migrations. No database changes run during request handling.

## Content and contact behaviour

Pages: Home, Solutions, Software, Hardware, Education, About, References, Careers, Contact. Careers accepts open applications without advertising invented vacancies. Gennext “Book a demo” links preselect the demo topic; confirmation means a request was received, not that a meeting was booked.

Contact topics: general, demo, software, hardware, education and career. Full-card links select the relevant form topic; without JavaScript they retain complete mailto drafts. The form itself requires JavaScript; email/phone alternatives remain available. Callback requests require a phone number. Career applicants can optionally share an HTTP(S) CV/portfolio URL; no upload is required.

The contact API stores validated enquiries in D1. It records marketing yes/no separately, alongside the exact displayed consent wording, version and opt-in timestamp. The checkbox is optional and unchecked initially. There is no campaign sending or automatic email notification integration. Messages are read at `/inbox`; Sites identity headers and the configured owner email authorize every inbox request. The platform database viewer also provides access to records.

Required hosted secrets: `INBOX_OWNER_EMAIL`, `FORM_RATE_LIMIT_SALT`. Keep values out of source. Identity is supplied by Sites, never accepted from form fields. Contact submissions enforce same-origin JSON requests, bounded input, a honeypot and hourly throttling. Daily salted client digests support throttling; raw IP addresses are not stored. Request IDs prevent duplicate inserts on retries. Failures never display a received confirmation; form contents stay available to retry. Inbox content is rendered as text, not HTML.

Gennext is Geniva's software product, linked contextually and in the footer, without a header product button. Longevity includes automated analysis/reporting through Gennext, with the laboratory as supporting capacity. No team section. Phone: +90 216 250 4471. Email: info@gennext.bio. The top-right Contact Us action remains visible on mobile; language links move into the mobile menu on small screens.

## Media and references

The approved 17 references and 7 citations are preserved. DETAE and Portakal logo sources are recorded in the reference JSON. Original publication titles remain unchanged. The Gennext interface and server illustrations are representative; the laboratory photo is the single supplied project image. Brochures are the supplied TR/EN PDFs. YouTube introduction: bQ-PGMYtemI.

## Validation and publication

```
python3 check_site.py
python3 check_responsive.py
GENIVA_QA_MODULES=/tmp/geniva-site-qa/node_modules node check_interactions.cjs
node check_worker.mjs
node --check app.js
```

The optional DOM checks use jsdom; CSS checks use lxml, tinycss2 and cssselect2. Worker tests use Node 22 SQLite with the D1 API shape and the actual generated migrations. Tests cover routing, bilingual content, form topics, consent, retries, validation, throttling, failure behaviour and inbox authorization. They never create test messages in the hosted inbox.

Browser visual and browser-native interaction checks remain unavailable in the current environment. Static CSS and DOM checks do not replace rendered browser QA.

The existing Sites project and owner-private access are preserved; indexing remains disabled. Publication does not change the company's external domains.
