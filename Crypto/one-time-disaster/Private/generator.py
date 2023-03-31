import binascii

def xor_strings(s1, s2):
    return ''.join(hex(ord(a) ^ ord(b))[2:].zfill(2) for a, b in zip(s1, s2))

def generate_cipher(flag, key):
    return xor_strings(flag, key)

flag = "accessdenied{n3v3r_r3p347_k3y5}"
key = "3141592653589793238462643383279502884197"

cipher1 = generate_cipher(flag, key)
cipher2 = generate_cipher("RevelationIsComputerScienceDepartment", key)

with open("cipher1.txt", "w") as f1, open("cipher2.txt", "w") as f2, open("key1.txt", "w") as k1, open("key2.txt", "w") as k2:
    f1.write(cipher1)
    f2.write(cipher2)
    k1.write(key)
    k2.write(key)