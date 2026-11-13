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

All eight pages checked in browser at 360px and 1440px: no horizontal overflow or broken loaded images. Mobile navigation, Escape, image dialog, and language switch checked. Static link/asset/fragment checks run by check_site.py.
