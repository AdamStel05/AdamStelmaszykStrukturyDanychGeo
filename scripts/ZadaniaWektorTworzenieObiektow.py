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

