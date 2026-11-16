# Mobile compatibility review - 16 November 2026

Status: automated CSS and DOM checks passed. Browser rendering and physical-device validation remain unverified because neither the connected Browser tool nor a cloud browser tool is available in this session. No browser installation or substitute browser automation was attempted.

## Coverage

All 9 English and 9 Turkish content pages were checked at 320, 360, 375, 390, 414, 430, 599, 600, 601, 759, 760, 761, 768, 820, 960, 1024, 1100, 1101 and 1440 CSS pixels: 342 page/width combinations. The widths around 600, 760 and 1100 check both sides of the layout transitions.

The static checks confirm:

- A device-width viewport with zoom allowed.
- The persistent Contact Us action and mobile menu declare 44px minimum heights.
- The mobile menu uses the dynamic viewport height and permits vertical scrolling.
- Language links move into the menu at 600px and below.
- Contact fields use 16px type, minimum 48px heights and shrinkable full widths; rows stack at 600px and below.
- The demo card spans the grid and stacks vertically at 760px and below.
- The Gennext logo retains its aspect ratio; images have maximum-width constraints and video uses a responsive 16:9 frame.
- Solutions, Education, Careers, references, hardware and analysis workflows switch to the intended narrow-screen layouts.

DOM tests cover menu toggling, Escape, focus wrapping, desktop-resize cleanup, language links, demo and career selection, callback validation, explicit marketing consent, submission success/failure, retries and clipboard fallback. Focus wrapping is tested with modeled visibility; jsdom does not measure rendered rectangles.

## Correction

Topic cards previously focused the name input immediately. That can trigger the virtual keyboard before the visitor has chosen to type. They now focus the selected form heading and scroll to the form, preserving keyboard/screen-reader context without focusing a text input.

## Limits

These checks do not prove absence of horizontal overflow, text clipping, browser-specific layout issues, viewport changes caused by a virtual keyboard, or touch/scroll behaviour on a physical phone. Safari/Chrome rendering, portrait/landscape screenshots and actual device interactions still need browser access. No hosted test messages were created.

## Reproduce

```sh
npm run build
python3 check_site.py
python3 check_responsive.py
GENIVA_QA_MODULES=/tmp/geniva-site-qa/node_modules node check_interactions.cjs
node --check app.js
git diff --check
```

The Python responsive check uses lxml, tinycss2 and cssselect2. The DOM check uses jsdom; set `GENIVA_QA_MODULES` to its installed node_modules directory when outside the project.
