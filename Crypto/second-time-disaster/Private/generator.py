import binascii

def xor_strings(s1, s2):
    return ''.join(hex(ord(a) ^ ord(b))[2:].zfill(2) for a, b in zip(s1, s2))

flag = "accessdenied{wh0_54y5_51z3_d035n07_m4773r}"
org_key = "tinykey"
key = org_key
while len(key) < len(flag):
    key += org_key

cipher = xor_strings(flag, key)
with open('cipher.txt', 'w') as f:
    f.write(cipher)

