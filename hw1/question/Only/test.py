import hlextend
from pwn import *
import signal
import sys
import os
import time
import base64
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

origin_text = "gjme123"

sha256 = SHA256.new()
sha256.update(origin_text)
print "origin ", sha256.digest().encode('hex')


k = hlextend.new('sha256')
k.hash(origin_text)

print "hlextend ver", k.hexdigest()


GG = hlextend.new('sha256')
padding = GG.extend('gg','jme123',1,k.hexdigest(),raw=True)
for i in padding:
    print i
"""
print "GG", GG.hexdigest()
sha256 = SHA256.new()
ans = ""
i =0
print "g"+padding
while i < len(padding):
    if padding[i] =='\\':
        if padding[i+2] == '8':
            ans+="\x80"
        else:
            ans+="\x00"
        i+=4
    else:
        ans+=padding[i]
        i+=1
print "g"+ans
sha256.update("g"+ans)
print "ans ", sha256.digest().encode('hex')
"""