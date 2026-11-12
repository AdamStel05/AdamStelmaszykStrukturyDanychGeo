import geopandas as gpd
from shapely import GeometryCollection, Point, LineString, MultiLineString, Polygon
from shapely.geometry import box

path_to_files = "dane/"

# Zadanie a

zones = gpd.read_file(path_to_files+"pl_pasy_ukształtowania.geojson")
zones2180 = zones.to_crs(epsg=2180)
zones2180["powierzchnia"] = zones2180.geometry.area
print(zones2180)

# Zadanie b

cities = gpd.read_file(path_to_files+"pl_miasta_wojewódzkie.geojson")
cities2180 = cities.to_crs(epsg=2180)
minX, minY, maxX, maxY = cities2180.total_bounds
bounding_box = box(minX, minY, maxX, maxX)
obwod_kilometry = bounding_box.length / 1000
print(obwod_kilometry)

# Zadanie c

rivers = gpd.read_file(path_to_files+"pl_rzeki.geojson")
rivers2180 = rivers.to_crs("EPSG:2180")
def liczenie_linii(geom):
  if geom is None or geom.is_empty:
    return 0
  if isinstance(geom, LineString):
    return 1
  elif isinstance(geom, MultiLineString):
    return len(geom.geoms)
  return 0
rivers2180["liczba_linii"] = rivers2180["geometry"].apply(liczenie_linii)
def liczenie_punktów(geom):
  if geom is None or geom.is_empty:
    return 0
  if isinstance(geom, LineString):
    return len(geom.coords)
  elif isinstance(geom, MultiLineString):
    return sum(len(line.coords) for line in geom.geoms)
  return 0
rivers2180["liczba_punktow"] = rivers2180["geometry"].apply(liczenie_punktów)
print(rivers2180)