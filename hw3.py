import sys
import hashlib
import binascii


f = open(sys.argv[1], 'rb')
blocks =[]
#Read the blocks
while True:
    block=f.read(256)
    if not block:
        break

    blocks.append(block)

#To get h0, we need to start from the end
blocks.reverse()

#for the last block, tag==None
tag=None

#Go through the blocks
for b in blocks:
    
    s = hashlib.sha256()

    if not tag:    
        s.update(b)    
        tag = s.hexdigest()
        continue
    
    s.update(b+tag.encode())
    tag=s.hexdigest()

print(tag)
f.close()