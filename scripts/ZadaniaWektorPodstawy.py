import geopandas as gpd
from shapely.geometry import MultiLineString
import matplotlib.pyplot as plt
import pandas as pd

path_to_files = "dane/"

# Zadanie a
rzeki = gpd.read_file(path_to_files+"hr1.geojson")
def liczenie(geometria):
    if isinstance(geometria, MultiLineString):
        return len(geometria.geoms)
    else:
        return 1
rzeki["liczba_czesci"] = rzeki["geometry"].apply(liczenie)
dwa_do_dziesiec = rzeki[(rzeki["liczba_czesci"] >= 2) & (rzeki["liczba_czesci"] <= 10)]
liczba_obiektow = len(dwa_do_dziesiec)
print(liczba_obiektow)

# Zadanie b
demografia = gpd.read_file(path_to_files+"lsp1.geojson")
demografia["procenty"] = pd.to_numeric(demografia["ludność_w_wieku_65_lat_i_więcej"], errors="coerce")
kraje_ponad_18 = demografia[demografia["procenty"] > 18]
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
kraje_ponad_18.plot(ax=ax, color='red', edgecolor='black')
plt.show()

# Zadanie c
wulkany = gpd.read_file(path_to_files+"wulkany/lw1/lw1.shp")
