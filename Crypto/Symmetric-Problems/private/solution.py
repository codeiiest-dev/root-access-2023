from Crypto.Cipher import AES


key = bytearray.fromhex('d24472f999afc6a2b9585dba605fc958')
IV = bytearray.fromhex('c1ed38370edcd57a956971736ccba6c1')

while True:
	encDec = AES.new(key, AES.MODE_CBC, IV)
	received = bytearray.fromhex(input('>> '))
	message = encDec.decrypt(received).decode().strip()
	print(message)

# accessdenied{k3y_exch4ng3_ru1n5_symm3tr1c_k3y_encryp7i0n}
