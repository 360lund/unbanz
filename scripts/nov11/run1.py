import sys; sys.path.insert(0,'/workspace/site/scripts/nov11')
import gen,b_tiktok,b_youtube,b_page,b_contact
for mod in (b_tiktok,b_youtube,b_page,b_contact):
    for p in mod.PAGES: gen.build(p)
import hubs
for p in hubs.H: gen.build(p)
open('/workspace/aeo_nov11/built1.txt','w').write('\n'.join(s for s,l,_ in gen.BUILT))
print(len(gen.BUILT))
