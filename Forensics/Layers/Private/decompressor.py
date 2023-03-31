import os, time

def unzip():
	os.system("unzip -p file > file2")
	os.system("rm file")
	os.system("mv file2 file")

def tar():
	os.system("tar -xvf file")

def bzip2():
	os.system("bzip2 -d file")
	os.system("mv file.out file")

def base64():
	os.system("base64 -d file > file2")
	os.system("rm file")
	os.system("mv file2 file")

def gzip():
	os.system("mv file file.gz")
	os.system("gzip -d file.gz")

def fileCommand():
	os.system("file file > shit")
	return open('shit', 'r').read()

while True:
	os.system('head file')
	if 'Zip archive data' in fileCommand():
		unzip()
		print('unzip')
	elif 'POSIX tar archive' in fileCommand():
		tar()
		print('tar')
	elif 'gzip compressed data' in fileCommand():
		gzip()
		print('gzip')
	elif 'bzip2 compressed data' in fileCommand():
		bzip2()
		print('bzip2')
	elif 'ASCII text' in fileCommand():
		base64()
		print('base64')
	time.sleep(0.1)
