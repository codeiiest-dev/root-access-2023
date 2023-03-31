import os, random

def zip_():
	os.system("zip -r file.zip file")
	os.system("rm file")
	os.system("mv file.zip file")

def tar():
	os.system("tar -czvf file.tar.gz file")
	os.system("rm file")
	os.system("mv file.tar.gz file")

def bzip2():
	os.system("bzip2 -z file")
	os.system("mv file.bz2 file")

def base64():
	os.system("base64 file > file2")
	os.system("rm file")
	os.system("mv file2 file")

for _ in range(100):
	if random.randint(0, 3) == 0:
		zip_()
		print('zip')
	elif random.randint(0, 3) == 1:
		tar()
		print('tar')
	elif random.randint(0, 3) == 2:
		bzip2()
		print('bzip2')
	else:
		base64()
		print('base64')
