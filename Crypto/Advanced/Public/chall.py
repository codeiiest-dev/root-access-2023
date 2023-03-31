# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import binascii, sys
from flag import flag

key = b"ah68skkx887b1h**" # Characters marked * are redacted
IV = flag

message = b"The future a dark desolate world.A world of war, suffering, loss"

def encrypt(message,passphrase):
	aes = AES.new(passphrase, AES.MODE_CBC, IV)
	return aes.encrypt(message)

print("Encrypted data: ", binascii.hexlify(encrypt(message,key)).decode())