import rasterio
import numpy as np
import matplotlib.pyplot as plt

path_to_files = "dane/raster/WlasnyRaster/sentinel-2-l2a_2026-08-16_S2C_MSIL2A_20260816T094031_R036_T34UEB_20260816T133909_"

# Zadanie a

with rasterio.open(path_to_files + "B04.tif") as src:
    red = src.read(1)
with rasterio.open(path_to_files + "B03.tif") as src:
    green = src.read(1)
with rasterio.open(path_to_files + "B02.tif") as src:
    blue = src.read(1)
rgb_stacked = np.stack([red, green, blue])
raster_rgb = np.moveaxis(rgb_stacked, 0, -1)
raster_rgb_norm = raster_rgb.astype(float).copy()
for i in range(3):
    low = np.percentile(raster_rgb_norm[:, :, i], 0.05)
    high = np.percentile(raster_rgb_norm[:, :, i], 99.95)
    raster_rgb_norm[:, :, i] = np.clip(
        (raster_rgb_norm[:, :, i] - low) / (high - low),
        0,
        1
    )
plt.imshow(raster_rgb_norm)
plt.axis("off")
plt.show()

# Zadanie b

plt.hist(raster_rgb_norm[:, :, 0].flatten(), bins=50)
plt.title("Histogram kanału czerwonego")
plt.show()
plt.hist(raster_rgb_norm[:, :, 1].flatten(), bins=50)
plt.title("Histogram kanału zielonego")
plt.show()
plt.hist(raster_rgb_norm[:, :, 2].flatten(), bins=50)
plt.title("Histogram kanału niebieskiego")
plt.show()
print("Histogram kanału czerwonego jest skoncentrowany między 0.0 a 0.6, kanału zielonego między 0.0 a 0.5, a niebieskiego między 0.0 a 0.4.")

# Zadanie c

with rasterio.open(path_to_files + "B04.tif") as src:
    red = src.read(1)
    transform = src.transform
wysokosc, szerokosc, _ = raster_rgb_norm.shape
czesc_w = wysokosc / 3
czesc_sz = szerokosc / 3
srodki = []
for r in range(3):
    for c in range(3):
        row_start = int(round(r * czesc_w))
        row_end = int(round((r + 1) * czesc_w))
        col_start = int(round(c * czesc_sz))
        col_end = int(round((c + 1) * czesc_sz))
        center_row = (row_start + row_end) / 2.0
        center_col = (col_start + col_end) / 2.0
        x_geo, y_geo = rasterio.transform.xy(transform, center_row, center_col, offset='center')
        srodki.append({
            "numer_czesci": f"{r+1}-{c+1}",
            "wspolrzedne (X, Y)": (x_geo, y_geo)
        })
for item in srodki:
    print(f"{item['numer_czesci']} -> {item['wspolrzedne (X, Y)'][0]:.2f} X {item['wspolrzedne (X, Y)'][1]:.2f} Y")

# Zadanie d

rgb_to_save = np.moveaxis(raster_rgb_norm, -1, 0)
with rasterio.open(path_to_files + "B04.tif") as src:
    profile = src.profile
    print(profile)
    profile.update(
        count=3,
        dtype=rgb_to_save.dtype
    )
with rasterio.open(
    "dane/raster/WlasnyRaster/wlasny_raster_trzy_kanaly.tif",
    "w",
    **profile
) as dst:
    dst.write(rgb_to_save)