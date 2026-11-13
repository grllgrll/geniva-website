# Geniva — final website

Bilingual static corporate website. Editable copy/templates: `build.py`; styles: `styles.css`; interactions: `app.js`.

Build and verify:

```sh
python3 package_site.py
python3 check_site.py
```

`dist/` contains the deployable website. Preview: `python3 -m http.server 8769 --bind 127.0.0.1 --directory dist`.

## Content decisions

- Main message: “Genomik veriyi anlamlandırıyoruz.” Multi-omics remains supporting content.
- Team and advisory profiles are removed.
- Contact address, email, telephone, and YouTube destination are sourced from Gennext Somatic Brochure v19, page 8. Source QR target: https://www.youtube.com/@GennextCommunity.
- PDFs are the supplied Turkish and English v19 brochures.
- Contact actions use mailto, tel, and maps links. No simulated form submission or unsolicited data collection.
- YouTube is an external link; no third-party video embeds or analytics.
- Brochure artwork is conceptual. Product screenshot is from the existing brochure assets.
- Current deployment is owner-private and deliberately not indexed. This does not replace the existing corporate domain.

## Verification

All ten pages checked in browser at 360px and 1440px: no horizontal overflow or broken loaded images. Mobile navigation, Escape, image dialog, and language switch checked. Static link/asset/fragment checks run by check_site.py.

## Content expansion

`enhancements.py` defines the clearer service routes, conceptual platform view, longevity laboratory photo slots and references page in both languages. Lab photographs can replace `.lab-photo-placeholder[data-photo-slot="microarray"]` and `[data-photo-slot="long-read"]`. No real lab photographs are claimed.

Reference institutions and publication metadata: user-supplied Gennext_Company_Overview_EN.pptx, slides 10–13 and slide 13 speaker notes. Only study-specific contributions are stated. Seven publications are selected, distinguishing peer-reviewed articles, a preprint and abstracts.

Representative hardware image: user's uploaded ASUS AP201 Amazon HTML, `landingImage` / `data-old-hires`: https://m.media-amazon.com/images/I/91FW0IOXncL._AC_SL1500_.jpg. This represents the chassis, not a fixed offered machine specification.

Laboratory capability and metabolomics/lipidomics scope were supplied directly by the user. Local microarray and Nanopore laboratory work is described separately from the wider multi-omics approach.
