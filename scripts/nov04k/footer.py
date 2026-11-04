import glob,os,re
os.chdir('/workspace/site')
L='<a href="/meta-appeal-links-and-forms-directory/">Appeal links</a>'
n=miss=0;m=[]
for f in glob.glob('**/*.html',recursive=True):
    if f.startswith(('scripts/','node_modules/')): continue
    h=open(f,errors='ignore').read()
    if 'class="footer-links"' not in h or 'meta-appeal-links-and-forms-directory/">Appeal links' in h: 
        if 'class="footer-links"' not in h: m.append(f)
        continue
    k=h.find('class="footer-links"'); e=h.find('</div>',k)
    seg=h[k:e]
    g=seg.find('<a href="/guides/">Guides</a>')
    if g>=0: ins=k+g+len('<a href="/guides/">Guides</a>')
    else: ins=e
    h=h[:ins]+L+h[ins:]; open(f,'w').write(h); n+=1
print(n,'pages; no footer-links:',len(m),m[:8])
