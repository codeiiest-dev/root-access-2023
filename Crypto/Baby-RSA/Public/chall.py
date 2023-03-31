from Crypto.Util.number import bytes_to_long
from secrets import p, q, flag

n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)

pt = bytes_to_long(flag)
ct = pow(pt, e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'p - q = {p - q}')
print(f'ct = {ct}')