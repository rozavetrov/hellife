import noise
import numpy as np
from PIL import Image


# # Constants
WIDTH = 1920
HEIGHT = int(WIDTH/2)
SCALE = 54


blue = [65, 105, 225]
green = [34, 139, 34]
beach = [238, 214, 175]
snow = [255, 255, 255]
mountain = [139, 137, 137]

data = np.zeros((HEIGHT, WIDTH, 3), dtype="uint8")

for y in range(data.shape[0]):
    for x in range(data.shape[1]):
        value = noise.snoise2(x/SCALE,
                              y/SCALE,
                              octaves=6,
                              persistence=0.5,
                              lacunarity=1.75)
        if value < 0.2:
            data[y, x] = blue
        elif value < 0.25:
            data[y, x] = beach
        elif value < 0.55:
            data[y, x] = green
        elif value < 0.75:
            data[y, x] = mountain
        elif value < 1:
            data[y, x] = snow

Image.fromarray(data).save("figure.png")