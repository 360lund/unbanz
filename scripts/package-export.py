from pathlib import Path
import re,base64,mimetypes,json,zipfile,tempfile
root=Path(__file__).resolve().parents[1];dist=root/'dist'
def dataurl(f):
 mime=mimetypes.guess_type(f.name)[0] or 'application/octet-stream'
 return 'data:'+mime+';base64,'+base64.b64encode(f.read_bytes()).decode()
def asset_url(v,parent):
 return dist/v.lstrip('/') if v.startswith('/') else parent/v
def css_inline(f):
 css=f.read_text()
 return re.sub(r'url\([\"\x27]?([^\)\"\x27]+)[\"\x27]?\)',lambda m:'url("'+dataurl(asset_url(m[1],f.parent))+'")' if not m[1].startswith(('data:','http')) else m[0],css)
def inline(page):
 text=page.read_text()
 text=re.sub(r'<link rel="stylesheet" href="([^"]+)"[^>]*>',lambda m:'<style>'+css_inline(asset_url(m[1],page.parent))+'</style>',text)
 text=re.sub(r'<script src="([^"]+)"[^>]*></script>',lambda m:'<script>'+asset_url(m[1],page.parent).read_text().replace('</script','<\\/script')+'</script>',text)
 # Inline scripts must run after the page DOM exists.
 scripts=re.findall(r'<script>(.*?)</script>',text,re.S)
 text=re.sub(r'<script>.*?</script>','',text,flags=re.S)
 text=text.replace('</body>',''.join('<script>'+j+'</script>' for j in scripts)+'</body>')
 text=re.sub(r'<link rel="preload"[^>]+>','',text)
 text=text.replace('https://unbanz.com/assets/unbanz-share-v4.jpg','https://unbanz.com/unbanz-share-v4.jpg')
 text=text.replace('https://unbanz.com/assets/social-preview.png','https://unbanz.com/social-preview.png').replace('https://unbanz.com/assets/favicon.svg','https://unbanz.com/favicon.svg')
 text=re.sub(r'(href=")[^\"]*assets/favicon.svg',r'\1/favicon.svg',text)
 return text
out=Path('/workspace/scratch/15ecf305683b/unbanz-website.zip')
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as z:
 for folder in ['dist','api','tests','scripts','marketing']:
  for f in (root/folder).rglob('*'):
   if f.is_file():z.write(f,f.relative_to(root))
 for name in ['README.md','AI_STUDIO_HANDOFF.md','vercel.json','.env.example','.gitignore']:z.write(root/name,name)
 for src,name in [('index.html','index.html'),('unban/index.html','unban.html'),('username/index.html','username.html'),('ban/index.html','ban.html'),('admin/index.html','admin.html'),('apply/index.html','apply.html')]:z.writestr('phone-upload/'+name,inline(dist/src))
 for name in ['sitemap.xml','robots.txt']:z.write(dist/name,'phone-upload/'+name)
 for name in ['social-preview.png','unbanz-share-v4.jpg','favicon.svg']:z.write(dist/'assets'/name,'phone-upload/'+name)
 z.writestr('phone-upload/vercel.json',json.dumps({'framework':None,'buildCommand':'','outputDirectory':'.','cleanUrls':True,'trailingSlash':True,'headers':[{'source':'/admin(.*)','headers':[{'key':'X-Robots-Tag','value':'noindex, nofollow'}]}]},indent=2))
 z.writestr('phone-upload/README.md','''# Unbanz phone upload
Upload every file in this folder to the root of a GitHub repository. Then import the repo into Vercel. Other framework, no build command, output directory . (already configured).

Every HTML file is self-contained, with embedded assets. The paths /unban/, /username/, /ban/ and /admin/ are served via clean URLs. The application opens at /apply/. It uses a spacious desktop form and a focused two-step mobile flow. No automatic submission backend is included in this static edition. Connect Firebase via AI Studio before taking applications. Until then submission reports unavailable; email/WhatsApp contact links remain usable.

Admin password: preview. Demo-only interface, not security. Implement Firebase Authentication and admin access rules before displaying real leads. No real lead data is included.

The parent archive contains the editable source and optional Vercel email backend. Do not upload the ZIP itself expecting it to run.
''')
 z.write(root/'AI_STUDIO_HANDOFF.md','phone-upload/AI_STUDIO_HANDOFF.md')
print(out)
