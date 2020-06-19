from Crypto.Cipher import AES
from binascii import hexlify, unhexlify


key = unhexlify('140b41b22a29beb4061bda66b6747e14')
IV = unhexlify('000102030405060708090a0b0c0d0e0f')
ciphertext=unhexlify('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
#print(key)

decipher = AES.new(key, AES.MODE_CBC, IV)
plaintext = decipher.decrypt(ciphertext)
hexlify(plaintext)
print(plaintext)