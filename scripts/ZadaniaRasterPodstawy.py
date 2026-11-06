import rasterio
import numpy as np
import matplotlib.pyplot as plt

path_to_files = "dane/raster/"
with rasterio.open(path_to_files+"tucholski_fragment.tif") as src:
    raster = src.read()
print(raster)
print(raster.shape)

rgb = np.moveaxis(raster[0:3], 0, -1)
plt.imshow(rgb)
plt.show()

plt.imshow(raster[0], cmap="Reds")
plt.colorbar()
plt.axis("off")
plt.show()

path2 = path_to_files+"wybrzeze/sentinel-2-l2a_2026-06-26_S2C_MSIL2A_20260626T101021_R022_T33UXA_20260626T152309/sentinel-2-l2a_2026-06-26_S2C_MSIL2A_20260626T101021_R022_T33UXA_20260626T152309_"

with rasterio.open(path2 + "B04.tif") as src:
    red = src.read(1)

with rasterio.open(path2 + "B03.tif") as src:
    green = src.read(1)

with rasterio.open(path2 + "B02.tif") as src:
    blue = src.read(1)

rgb_stacked = np.stack([red, green, blue])
print(rgb_stacked)

raster_rgb = np.moveaxis(rgb_stacked, 0, -1)

plt.imshow(raster_rgb)
plt.axis("off")
plt.show()

raster_rgb1 = raster_rgb / raster_rgb.max() * 255
raster_rgb1 = raster_rgb1.astype(np.uint8)

plt.imshow(raster_rgb1) # Wartości 0-255
plt.axis("off")
plt.show()

raster_rgb2 = raster_rgb.astype(float).copy()
for i in range(3):
    low = np.percentile(raster_rgb2[:, :, i], 2)
    high = np.percentile(raster_rgb2[:, :, i], 98)

    raster_rgb2[:, :, i] = np.clip(
        (raster_rgb2[:, :, i] - low) / (high - low),
        0,
        1
    )

plt.imshow(raster_rgb2) # Wartości 0.0 - 1.0
plt.axis("off")
plt.show()