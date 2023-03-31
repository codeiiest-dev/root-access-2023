cipher = ''
with open('cipher.txt', 'r') as f:
    cipher = f.read()

cipher_arr = [int(cipher[i:i+2], 16) for i in range(0, len(cipher), 2)]

print(cipher_arr)

# prefix = 'accessdenied{'
# prefix_arr = [ord(c) for c in prefix]

# key = [prefix_arr[i] ^ cipher_arr[i] for i in range(len(prefix_arr))]

# print(key)
# print(''.join([chr(c) for c in key]))

key = 'tinykey'

key_arr = [ord(c) for c in key]

while len(key_arr) < len(cipher_arr):
    key_arr += key_arr

flag = [key_arr[i] ^ cipher_arr[i] for i in range(len(cipher_arr))]
print(''.join([chr(c) for c in flag]))