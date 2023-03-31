import hashlib
import time

block = open('block', 'r').read()

def append_nonce(block, nonce):
    return block + str(hex(nonce)[2:])

def mine(block, difficulty):
    nonce = 0
    while True:
        nonced_block = append_nonce(block, nonce)
        hash = hashlib.sha256(nonced_block.encode()).hexdigest()
        if hash.startswith('0' * difficulty):
            return nonced_block, hash, nonce
        nonce += 1
        
start = time.clock_gettime(time.CLOCK_MONOTONIC)
nonced_block, hash, nonce = mine(block, 7)
end = time.clock_gettime(time.CLOCK_MONOTONIC)

print(hash, nonce)

print('\n\n\n\Time taken:', end - start)