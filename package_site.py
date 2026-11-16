"""Build and package only the pages and assets used by the current site."""
from pathlib import Path
import re, shutil, json
from build import build
from contact_form import CONSENT
root=Path(__file__).resolve().parent
generated=build()
output=root/'dist'
# All contents of dist are generated; move the static site under the Worker assets.
if output.exists():shutil.rmtree(output)
dist=output/'client'
dist.mkdir(parents=True,exist_ok=True)
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
server=output/'server';server.mkdir()
source=(root/'worker/index.mjs').read_text()
source=source.replace('__CONSENT_TEXT__',json.dumps(CONSENT,ensure_ascii=False)).replace('__INBOX_HTML__',json.dumps((root/'worker/inbox.html').read_text(),ensure_ascii=False))
(server/'index.js').write_text(source)
(server/'wrangler.json').write_text(json.dumps({
 'name':'geniva-web','main':'index.js','compatibility_date':'2026-11-16',
 'assets':{'directory':'../client','binding':'ASSETS','run_worker_first':True,'html_handling':'none'},
 'd1_databases':[{'binding':'DB','database_name':'site-creator-d1','database_id':'00000000-0000-4000-8000-000000000000'}],
},indent=2)+'\n')
metadata=output/'.openai';metadata.mkdir()
shutil.copy2(root/'.openai/hosting.json',metadata/'hosting.json')
shutil.copytree(root/'drizzle',metadata/'drizzle')
print('Packaged site, contact Worker and database migrations; existing private access retained.')
