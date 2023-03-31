import numpy as np
from PIL import Image as im

file = open('1.PNG', 'rb')
data = np.array([int(_) for _ in file.read()])

x = int(len(data) ** 0.5)
while len(data) % x != 0:
    x += 1
y = len(data) // x

image = np.reshape(np.array(np.zeros(x * y)), (x, y))

i1, i2, j2 = 0, 0, 1

while i2 != len(image):
    i, j = i2, 0
    while i != -1 and j != len(image[0]):
        image[i][j] = int(data[i1])
        i -= 1
        j += 1
        i1 += 1
    i2 += 1

while j2 != len(image[0]):
    i, j = len(image) - 1, j2
    while i != -1 and j != len(image[0]):
        image[i][j] = int(data[i1])
        i -= 1
        j += 1
        i1 += 1
    j2 += 1

intImage = []

for i in image:
    intImage.append([int(_) for _ in i])

intImage = np.array(intImage)

image = im.fromarray(np.array(intImage))
image.save('collectedData.png')