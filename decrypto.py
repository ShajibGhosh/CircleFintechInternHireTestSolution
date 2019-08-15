# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:30:29 2019

@author: Shajib Ghosh
"""

import base64
import hashlib
from Crypto.Cipher import AES

unpad = lambda s: s[:-ord(s[len(s) - 1:])]
 
password = 'a1b2c3d4e5f6g7h8'
 
 
 
def decrypt(enc, password):
    private_key = hashlib.sha256(password.encode("utf-8")).digest()
    enc = base64.b64decode(enc)
    iv = enc[:16]
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[16:]))
 
 

encrypted = b'3Jgrnid0Y+JrqsxpWZ0q3w3UqpH6GEy4Fh27thLMUM0A82fHf2D6sl7AboKFcyOA'
 
# Let us decrypt using our original password
decrypted = decrypt(encrypted, password)
print(bytes.decode(decrypted))