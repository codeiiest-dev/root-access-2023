import socket, random, os, time
from Crypto.Cipher import AES

key = os.urandom(16)
IV = os.urandom(16)
mode = AES.MODE_CBC

def padding(message):
    return message + ' ' * (16 - len(message) % 16)		

s = socket.socket()		
print ("Socket successfully created")

port = 12344		

s.bind(('', port))		
print ("socket binded to %s" %(port))

s.listen(5)	
print ("socket is listening")		

while True:
	c, addr = s.accept()	
	print ('Got connection from', addr )
	c.send('Thank you for connecting'.encode())
	time.sleep(1)
	c.send(key)
	time.sleep(1)
	c.send(IV)
	
	while True:
		encDec = AES.new(key, AES.MODE_CBC, IV)
		message = encDec.decrypt(c.recv(1024)).decode().strip()
		print (message)
		
		encDec = AES.new(key, AES.MODE_CBC, IV)
		qwerty = str.encode(padding(input('>>').strip()))
		c.send(encDec.encrypt(qwerty))
	
	c.close()
	break
