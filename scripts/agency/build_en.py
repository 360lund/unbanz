import sys; sys.path.insert(0,'.')
import importlib
from lib import *
MODS = ['c1_core','c2_audience','c3_services','c4_ops','c5_hubs','c6_extra']
for m in MODS:
    try: importlib.import_module(m)
    except ModuleNotFoundError as e:
        if e.name != m: raise
if __name__ == '__main__':
    for s in REG.values(): build_en(s)
    print(len(REG),'built')
