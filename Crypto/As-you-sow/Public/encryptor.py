import datetime
import random


data = open('flag.PNG', 'rb').read()
buffer = 16 - len(data) % 16

data += bytes([0 for _ in range(buffer - 1)] + [buffer])
data = [int(_) for _ in data]

matrix = []
for i in range(0, len(data), len(data) // 16):
    matrix.append(data[i:i + len(data) // 16])

key = [[random.randint(0, 255) for _ in range(3)] for __ in range(3)]

for i in range(len(matrix) - 2):
    for j in range(len(matrix[0]) - 2):
        for i1 in range(3):
            for j1 in range(3):
                matrix[i + i1][j + j1] ^= key[i1][j1]


x = str(datetime.datetime.now())
seed = int(x[:4] + x[5:7] + x[8:10] + x[11:13] + x[14:16])
random.seed(seed)

shuffler = list(range(16))
random.shuffle(shuffler)

encrypted = [[] for _ in range(len(matrix))]

for i in range(len(matrix)):
    encrypted[shuffler[i]] = matrix[i]

print(key)
print(encrypted)