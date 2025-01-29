import geopandas as gpd
import sys
import json
from topojson import Topology
import requests
from pathlib import Path

lake_champlain = gpd.read_file("src/VT_Lake_Champlain_(extracted_from_VHDCARTO)_-_polygon.geojson")

topo_1 = Topology(lake_champlain).to_dict()

multi_topo = {
    "type": "Topology",
    "objects": {
        "lake": topo_1['objects']['data'],
    },
    "bbox": topo_1['bbox'],
    "transform": topo_1['transform'],
    "arcs": topo_1['arcs']
}

sys.stdout.write(json.dumps(multi_topo))