# Geniva website

English-first corporate site centred on **Software, Hardware and Training for health big data**.

## Editing and building

- `site_pages.py`: bilingual copy, service definitions and semantic page templates.
- `build.py`: shared navigation/footer, metadata, language routing and page generation.
- `styles.css`: shared design and responsive layouts.
- `app.js`: mobile menu, accessible dropdown handling, language switching, email copy and legacy section redirects.
- `assets/reference-data.json`: approved reference groups, logo provenance and original publication metadata.

Run with Python 3.10 or later:

```sh
python3 package_site.py
python3 check_site.py
node --check app.js
```

`dist/` is generated deployment output. Packaging copies only the media used by the current pages. `build.py` creates 16 content pages and 8 compatibility redirects. Optional local preview: `python3 -m http.server 8770 --bind 127.0.0.1 --directory dist`.

## Routes and content

English pages live at the root; Turkish pages are under `/tr/`. `/en/` redirects preserve existing English links, search parameters and fragments. Each language contains Home, Solutions, Software, Hardware, Training, About, References and Contact.

Solutions is an overview. Software contains Gennext, clinical genomics, longevity automation/reporting, laboratory support and the YouTube introduction. Hardware contains Worker Node/server imagery, capacity planning and the precise federation diagram. Training describes audience, scope, learning outcomes and community resources.

Old Solutions section links are forwarded to the respective detail pages. Language changes keep the current page and section. No browser-language auto-redirect or language preference storage overrides the English default.

The exact agreed homepage copy is:

> Software, hardware and training for health big data.
>
> We develop software, build computing infrastructure and provide training for health data analysis, interpretation and reporting.

Gennext is Geniva's software product. Its own site is linked contextually and in the footer. No Gennext button appears in the header. Longevity includes automated data analysis and reporting through Gennext; the laboratory is supporting capacity. No team section is included.

## Sources and media

Reference groups and publications come from the supplied company presentation and the user's corrections. Original article titles are preserved, including the word “insights” in one article title; marketing copy does not use it. The previously removed seven references stay excluded.

The DETAE and Portakal Klinik logos were retrieved from their official websites; source URLs are recorded in the reference data. Existing logos and publications retain their provenance. The Gennext interface and server illustrations are representative, not patient data or hardware specifications. The laboratory photo is the single supplied project image. Brochures are the provided TR/EN PDFs.

Contact: info@gennext.bio, +90 216 250 4471, Acıbadem University TEKMER, Istanbul. Contact actions use mailto/tel/maps links; no simulated submission or analytics. The YouTube video is embedded on Software; Training links to the channel.

## Verification and hosting

`check_site.py` checks routing, language counterparts, local assets and fragments, accessible image text, page structure, reference counts and agreed content constraints. `check_responsive.py` checks computed CSS cascade rules at selected screen widths without launching a browser.

`check_interactions.cjs` runs DOM-level checks with optional `jsdom@26.1.0`: menu state, Escape, resize cleanup, dropdown closure, language destinations, clipboard handling and legacy redirects. Set `GENIVA_QA_MODULES` to the node_modules directory containing jsdom when it is installed outside the project.

Browser visual and interaction QA could not be performed in the November 16 environment because browser preview was unavailable. Static checks are not a substitute for a browser rendering check.

The existing Sites project and owner-private access are preserved; indexing remains disabled. Publication does not change the company's external domains.
