flag="accessdenied{7r4c1n6_15_d0p3}"

values = [0x40, 0x41, 0x42]

def init_values():
    for i in range(0, len(values)) :
        values[i] = ((values[i] << 2) | (values[i] >> 6)) ^ 0x42

init_values()

print(values)


for i in range(0, len(flag)) :
    print(hex(values[i%3] ^ ord(flag[i])), end=', ')