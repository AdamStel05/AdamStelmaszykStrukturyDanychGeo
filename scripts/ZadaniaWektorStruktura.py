import geopandas as gpd

path_to_files = "../dane/"
cities = gpd.read_file(path_to_files+"pl_miasta_wojewódzkie.geojson")

cities.to_file("dane.gpkg")

cities.to_csv("dane.csv", 
    index=False, 
    sep=";",
    decimal=",",
    encoding="utf-8")
cities.to_csv("dane.txt", index=False)

print(cities.iloc[0].geometry.geom_type)

print(cities.iloc[0].geometry)
print(cities.iloc[0].geometry.x)
print(cities.iloc[0].geometry.y)

cities["x"] = cities.geometry.x
cities["y"] = cities.geometry.y
print(cities.head())

rivers = gpd.read_file(path_to_files+"pl_rzeki.geojson")
zones = gpd.read_file(path_to_files+"pl_pasy_ukształtowania.geojson")

print(rivers.iloc[0].geometry.length)
print(zones.iloc[0].geometry.length)

print(zones.iloc[0].geometry.area)
print(zones.iloc[0].geometry.centroid)

print(zones.iloc[0].geometry.bounds)
print(zones.iloc[0].geometry.envelope)

print(cities.crs)
print(cities.crs.name)
print(cities.crs.to_epsg())

cities.set_crs("EPSG:4326", inplace=True)
print(cities.crs) 

print(rivers.iloc[0].geometry.length)
rivers2 = rivers.to_crs("EPSG:2180")
print(rivers2.iloc[0].geometry.length)

cities.to_file(
    "polska.gpkg",
    layer="miasta"
)

rivers.to_file(
    "polska.gpkg",
    layer="rzeki"
)

zones.to_file(
    "polska.gpkg",
    layer="pasy_ukształtowania"
)

print(gpd.list_layers("polska.gpkg"))

pl = gpd.read_file(
    "polska.gpkg"
)
print(pl.head())

rivers3 = gpd.read_file(
    "polska.gpkg",
    layer="rzeki"
)
print (rivers3.head())

from shapely import GeometryCollection, Point, LineString, Polygon

geometry = GeometryCollection([
    Point(0, 0),
    LineString([(1, 1), (2, 2)]),
    Polygon([(3, 3), (3, 4), (4, 4), (4, 3)])
])

print(geometry)
print(geometry.geom_type)

gdf = gpd.GeoDataFrame(
    geometry=[geometry],
    crs="EPSG:4326"
)
print(gdf)
print(gdf.geom_type)

gdf2 = gpd.GeoDataFrame(
    geometry=list(geometry.geoms),
    crs="EPSG:4326"
)
print(gdf2)
print(gdf2.geom_type)

# Zadanie a

powierzchnie = area(zones, EPSG:2180)

# Zadanie b

bounding_box(cities)
obwod = circumference(bounding_box)