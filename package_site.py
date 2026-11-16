"""Build and package only the pages and assets used by the current site."""
from pathlib import Path
import re, shutil
from build import build
root=Path(__file__).resolve().parent
generated=build()
dist=root/'dist'
dist.mkdir(exist_ok=True)
for relative in generated:
 target=dist/relative
 target.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(root/relative,target)
for name in ['styles.css','app.js']:
 shutil.copy2(root/name,dist/name)
used={'FONT-LICENSE.txt'}
for relative in generated+[Path('styles.css')]:
 used.update(re.findall(r'assets/([a-zA-Z0-9_./-]+)',(root/relative).read_text()))
assets=dist/'assets'
assets.mkdir(exist_ok=True)
for name in used:
 target=assets/name
 target.parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(root/'assets'/name,target)
# dist is generated output; retired media must not survive a rebuild.
for old in assets.rglob('*'):
 if old.is_file() and str(old.relative_to(assets)) not in used:old.unlink()
expected=set(generated)
for old in dist.rglob('*.html'):
 if old.relative_to(dist) not in expected:old.unlink()
(dist/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Packaged English-first site in dist; existing private access and indexing policy retained.')
