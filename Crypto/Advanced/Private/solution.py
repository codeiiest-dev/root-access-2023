# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import binascii, sys

keyR = b"ah68skkx887b1h" # Character marked * are redacted

message = b"The future a dark desolate world.A world of war, suffering, loss"
ct = bytes.fromhex("056ea4e6becdf223951bbed86494121d4a48dc1914c743a6e829b68c80eba1a362c98fbe4a2a28cb903f0cd0139b14cf93c3a8530cb74f921820c940f681ebed")

ptArr = []
ctArr = []

for i in range(0, len(message), 16):
    ptArr.append(message[i:i + 16])
for i in range(0, len(ct), 16):
    ctArr.append(ct[i:i + 16])

key = b''
for i in range(256):
    found = 0
    for j in range(256):
        key = keyR + bytes([i, j])
        aes = AES.new(key, AES.MODE_CBC, ctArr[-2])
        if aes.decrypt(ctArr[-1]) == ptArr[-1]:
            found = 1
            break
    if found:
        break

aes = AES.new(key, AES.MODE_ECB)
ptXor = aes.decrypt(ctArr[0])

for i in range(16):
    print(chr(ptXor[i] ^ message[i]), end = '')


# from Crypto.Cipher import AES
# import binascii, sys
# # from flag import flag

# key = b"ah68skkx887b1hjZ"
# IV = b'AES_CBC_ov3r_ECB'

# message = b"The future a dark desolate world.A world of war, suffering, loss"

# def encrypt(message,passphrase):
# 	aes = AES.new(passphrase, AES.MODE_CBC, IV)
# 	return aes.encrypt(message)

# print("Encrypted data: ", binascii.hexlify(encrypt(message,key)).decode())