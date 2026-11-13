"""Build the bilingual static site and its deployment directory."""
from pathlib import Path
import re, runpy, shutil
root=Path(__file__).resolve().parent
runpy.run_path(str(root/'build.py'))
dist=root/'dist'
dist.mkdir(exist_ok=True)
for page in root.glob('*.html'): shutil.copy2(page,dist/page.name)
shutil.copytree(root/'en',dist/'en',dirs_exist_ok=True)
for name in ['styles.css','app.js']:shutil.copy2(root/name,dist/name)
assets=dist/'assets';assets.mkdir(exist_ok=True)
used={'FONT-LICENSE.txt'}
for p in list(dist.glob('*.html'))+list((dist/'en').glob('*.html'))+[dist/'styles.css']:
 used.update(re.findall(r'assets/([a-zA-Z0-9_./-]+)',p.read_text()))
for name in used:
 (assets/name).parent.mkdir(parents=True,exist_ok=True)
 shutil.copy2(root/'assets'/name,assets/name)
(dist/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
print('Packaged static site in dist; private review publication, indexing disabled.')
