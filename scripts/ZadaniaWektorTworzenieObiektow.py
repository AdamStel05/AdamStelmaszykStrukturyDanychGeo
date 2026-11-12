from shapely import Point, LineString, Polygon
import geopandas as gpd
from shapely import MultiLineString
import matplotlib.pyplot as plt

# Zadanie a

A1 = LineString([
    (10, 10),
    (13, 20),
    (16, 10),
    (14.5, 15),
    (11.5, 15)
])
D = LineString([
    (17, 10),
    (17, 20),
    (23, 18),
    (23, 12),
    (17, 10)
])
A2 = LineString([
    (24, 10),
    (27, 20),
    (30, 10),
    (28.5, 15),
    (25.5, 15)
])
S = LineString([
    (37, 20),
    (31, 20),
    (31, 16),
    (37, 14),
    (37, 10),
    (31, 10)
])
T = LineString([
    (38, 20),
    (44, 20),
    (41, 20),
    (41, 10)
])
E = LineString([
    (51, 20),
    (45, 20),
    (45, 15),
    (51, 15),
    (45, 15),
    (45, 10),
    (51, 10)
])
multiline = MultiLineString([A1, D, A2, S, T, E])
gdfA1 = gpd.GeoDataFrame(
    {
        "name": ["Multilinia"]
    },
    geometry=[multiline],
    crs="EPSG:2180"
)
gdfA1.plot()
plt.show()
gdfA1.to_file("dane/adaste.gpkg")

# Zadanie b

wyspy = gpd.read_file("dane/fw2.geojson")
slownik = {}
for index, row in wyspy.iterrows():
    panstwo = row["państwo"]
    geometria = row['geometry']
    if panstwo not in slownik:
        slownik[panstwo] = []
    slownik[panstwo].append(geometria)
powierzchnie_panstw = {}
for panstwo, lista_geometrii in slownik.items():
    suma_powierzchni = sum(geom.area for geom in lista_geometrii)
    powierzchnie_panstw[panstwo] = suma_powierzchni
Top_10 = sorted(powierzchnie_panstw.items(), key=lambda x: x[1], reverse=True)[:10]
print(Top_10)

# Zadanie c

Japonia = wyspy[wyspy["państwo"] == "Japonia"]
def count_geometry_elements(Japonia):
    total_vertices = 0
    total_edges = 0
    for geom in Japonia.geometry:
        polygons = geom.geoms if geom.geom_type == 'MultiPolygon' else [geom]
        for poly in polygons:
            ext_coords = len(poly.exterior.coords) - 1
            total_vertices += ext_coords
            total_edges += ext_coords
            for interior in poly.interiors:
                int_coords = len(interior.coords) - 1
                total_vertices += int_coords
                total_edges += int_coords        
    return total_vertices, total_edges
tolerances = [0.5, 0.1, 0.01]
titles = [
    "Poziom 1: Wysokie uproszczenie (tol = 0.5)",
    "Poziom 2: Średnie uproszczenie (tol = 0.1)",
    "Poziom 3: Niskie uproszczenie (tol = 0.01)"
]
fig, axes = plt.subplots(1, 3, figsize=(16, 6))
for i, tol in enumerate(tolerances):
    uproszczone = Japonia.copy()
    uproszczone["geometry"] = Japonia.geometry.simplify(tolerance=tol, preserve_topology=True)
    vertices, edges = count_geometry_elements(uproszczone)
    ax = axes[i]
    uproszczone.plot(ax=ax, color="#4A90E2", edgecolor="black", linewidth=0.8)
    ax.set_title(f"{titles[i]}\nWierzchołki: {vertices} | Krawędzie: {edges}", fontsize=10)
    ax.set_xlabel("Długość geograficzna")
    ax.set_ylabel("Szerokość geograficzna")
plt.tight_layout()
plt.show()