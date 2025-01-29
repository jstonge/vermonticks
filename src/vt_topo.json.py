import geopandas as gpd
import sys
import json
from topojson import Topology
import requests
from pathlib import Path


# VERMONT

url="https://raw.githubusercontent.com/vprnet/vermont-map/refs/heads/master/vermont.json"
TMPDIR = Path('src/.observablehq/cache/vt_topo.json')
r = requests.get(url=url,  headers={'User-Agent': 'Mozilla/5.0'})
if not TMPDIR.exists():
    with open(TMPDIR, 'wb') as f:
        f.write(r.content)

districts = gpd.read_file(TMPDIR)


topo_1 = Topology(districts).to_dict()

multi_topo = {
    "type": "Topology",
    "objects": {
        "state": topo_1['objects']['data'],
    },
    "bbox": topo_1['bbox'],
    "transform": topo_1['transform'],
    "arcs": topo_1['arcs']
}

sys.stdout.write(json.dumps(multi_topo))