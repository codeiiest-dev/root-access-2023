import socket
from Crypto.Cipher import AES		

s = socket.socket()		
port = 12344

s.connect(('127.0.0.1', port))

def padding(message):
    return message + ' ' * (16 - len(message) % 16)		

print (s.recv(1024).decode())
key = s.recv(1024)
IV = s.recv(1024)
print(key, IV)

# encDec = AES.new(key, AES.MODE_CBC, IV)

while True:
	encDec = AES.new(key, AES.MODE_CBC, IV)
	qwerty = str.encode(padding(input('>>').strip()))
	s.send(encDec.encrypt(qwerty))
	
	encDec = AES.new(key, AES.MODE_CBC, IV)
	message = encDec.decrypt(s.recv(1024)).decode().strip()
	print (message)

s.close()
