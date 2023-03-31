import binascii

cipher1=''
cipher2=''

def xor_strings(s1, s2):
    a = [int(s1[i:i+2], 16) for i in range(0, len(s1), 2)]
    b = [int(s2[i:i+2], 16) for i in range(0, len(s2), 2)]
    return ''.join(hex(a^b)[2:] for a, b in zip(a, b))

with open("cipher1.txt", "r") as f1, open("cipher2.txt", "r") as f2:
    cipher1 = f1.read()
    cipher2 = f2.read()


combined_cipher = xor_strings(cipher1, cipher2)

message1 = "accessdenied{"
message2 = ""
key = ''

cipher1_hex = [int(cipher1[i:i+2], 16) for i in range(0, len(cipher1), 2)]
cipher2_hex = [int(cipher2[i:i+2], 16) for i in range(0, len(cipher2), 2)]
message1_hex = [ord(message1[i]) for i in range(len(message1))]
message2_hex = [ord(message2[i]) for i in range(len(message2))]
key_hex = [ord(key[i]) for i in range(len(key))]
combined_cipher_hex = [int(combined_cipher[i:i+2], 16) for i in range(0, len(combined_cipher), 2)]

print("Cipher1:", cipher1)
print("Cipher1 Hex:", str(cipher1_hex))
print("Cipher2:", cipher2)
print("Cipher2 Hex:", str(cipher2_hex))
print("Combined Cipher Hex:", str(combined_cipher_hex))
print("Message1:", message1)
print("Message1 Hex:", str(message1_hex))
print("Message2:", message2)
print("Message2 Hex:", str(message2_hex))
print("Key:", key)
print("Key Hex:", str(key_hex))

# verification of known information
length = min(len(message1_hex), len(combined_cipher_hex), len(message2_hex), len(key_hex))
print("\nVerifying till length:", length)
for i in range(length):
    exp_cipher1 = message1_hex[i] ^ key_hex[i]
    exp_cipher2 = message2_hex[i] ^ key_hex[i]

    if exp_cipher1 != cipher1_hex[i]:
        print("Cipher1 mismatch at index", i, "expected", exp_cipher1, "got", cipher1_hex[i])
    if exp_cipher2 != cipher2_hex[i]:
        print("Cipher2 mismatch at index", i, "expected", exp_cipher2, "got", cipher2_hex[i])

max_length = max(len(message1_hex), len(message2_hex), len(key_hex))
print("\nMax length:", max_length)

if (max_length == len(message1_hex)):
    length = len(message1_hex)
    print("\nGuessing with message 1...")
    key_hex = [(cipher1_hex[i]^message1_hex[i]) for i in range(length)]
    message2_hex = [(cipher2_hex[i]^key_hex[i]) for i in range(length)]

if (max_length == len(message2_hex)):
    length = min(len(cipher1_hex), len(message2_hex))
    print("\nGuessing with message 2...")
    key_hex = [(cipher2_hex[i]^message2_hex[i]) for i in range(length)]
    message1_hex = [(cipher1_hex[i]^key_hex[i]) for i in range(length)]

if (max_length == len(key_hex)):
    length = len(key_hex)
    print("\nGuessing with key...")
    message1_hex = [(cipher1_hex[i]^key_hex[i]) for i in range(length)]
    message2_hex = [(cipher2_hex[i]^key_hex[i]) for i in range(length)]

key = ''.join(chr(i) for i in key_hex)
decode1 = ''.join(chr(i) for i in message1_hex)
decode2 = ''.join(chr(i) for i in message2_hex)

print("Key", key)
print("Decoded Cipher1:", decode1)
print("Decoded Cipher2:", decode2)

# for i in range(len(message1)):
#     decode1 += message1[i]
#     key += chr(ord(message1[i]) ^ int(cipher1[i * 2:(i * 2) + 2], 16))
#     decode2 += chr(int(cipher2[i * 2:(i * 2) + 2], 16) ^ ord(key[i]))

# print("Key: " + key)
# print("Decoded Cipher1: " + decode1)
# print("Decoded Cipher2: " + decode2)