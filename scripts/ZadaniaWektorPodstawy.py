import geopandas as gpd

path_to_files = "C:/Users/stelm/Downloads/Piąty semestr/"

shp_v = gpd.read_file(path_to_files+"wulkany/lw1/lw1.shp")
print(shp_v.head())

geojson_v = gpd.read_file(path_to_files+"wulkany/lw1.geojson")
print(geojson_v.head())

gpkg_v = gpd.read_file(path_to_files+"wulkany/lw1.gpkg")
print(gpkg_v.head())

rzeki = gpd.read_file(path_to_files+"hr1.geojson")
print(rzeki.head())

x = 0
for i in rzeki:
    if i.MultiLineString > 2 and i.MultiLineString < 10:
        x = x + 1

kraje = gpd.read_file(path_to_files+"lsp1.geojson")
print(kraje.head())

for i in kraje:
    if i$ludność_w_wieku_65_lat_i_więcej > 18:
        select(i)

usa = filter(shp_v, kraj="Stany Zjednoczone")