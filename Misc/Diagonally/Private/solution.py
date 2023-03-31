# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image as im

pic = im.open("collectedData.png")
image = np.array(pic.getdata()).reshape(pic.size[1], pic.size[0])

data = [0 for _ in range(pic.size[1] * pic.size[0])]

i1, i2, j2 = 0, 0, 1

while i2 != len(image):
    i, j = i2, 0
    while i != -1 and j != len(image[0]):
        data[i1] = image[i][j]
        i -= 1
        j += 1
        i1 += 1
    i2 += 1

while j2 != len(image[0]):
    i, j = len(image) - 1, j2
    while i != -1 and j != len(image[0]):
        data[i1] = image[i][j]
        i -= 1
        j += 1
        i1 += 1
    j2 += 1

open("flag", 'wb').write(bytes(data))