#!/usr/bin/env python
from pwn import *
import hashlib
import os
import random
import signal
import sys
import time
h1 ="7346dc9166b67e118f029ab621b2560ff9ca67cca8c7f85ba84c79030c2b3de218f86db3a90901d5df45c14f26fedfb3dc38e96ac22fe7bd728f0e45bce046d23c570feb141398bb552ef5a0a82be331fea48037b8b5d71f0e332edf93ac3500eb4ddc0decc1a864790c782c76215660dd309791d06bd0af3f98cda4bc4629b1".decode("hex")
h2 ="7f46dc93a6b67e013b029aaa1db2560b45ca67d688c7f84b8c4c791fe02b3df614f86db1690901c56b45c1530afedfb76038e972722fe7ad728f0e4904e046c230570fe9d41398abe12ef5bc942be33542a4802d98b5d70f2a332ec37fac3514e74ddc0f2cc1a874cd0c78305a21566461309789606bd0bf3f98cda8044629a1".decode("hex")
common_pre="2550 4446 2d31 2e33 0a25 e2e3 cfd3 0a0a0a31 2030 206f 626a 0a3c 3c2f 5769 64746820 3220 3020 522f 4865 6967 6874 20332030 2052 2f54 7970 6520 3420 3020 522f5375 6274 7970 6520 3520 3020 522f 46696c74 6572 2036 2030 2052 2f43 6f6c 6f725370 6163 6520 3720 3020 522f 4c65 6e677468 2038 2030 2052 2f42 6974 7350 6572436f 6d70 6f6e 656e 7420 383e 3e0a 73747265 616d 0aff d8ff fe00 2453 4841 2d312069 7320 6465 6164 2121 2121 2185 2fec0923 3975 9c39 b1a1 c63c 4c97 e1ff fe01".replace(" ","").decode("hex")

def sha1(content):
    Hash=hashlib.sha1()
    Hash.update(content)
    return Hash.digest()

def find_hex(string):
    i = 0
    while True:
        UserHash=sha1(common_pre+h1+str(i)).encode("hex")
        #UserHash=sha1(str(i)).encode("hex")
        if UserHash[-6:] == "{:0>6}".format(string):
            break 
        i+=1
    return str(i)

def solve():
    conn = remote("140.112.31.109",10001)
    k = conn.recvuntil(':')[-7:-1]
    i = find_hex(k)
    conn.sendline((common_pre+h2+i).encode("hex"))
    gg =  conn.recvline()
    if "faster" in gg:
        return 0
    conn.sendline((common_pre+h1+i).encode("hex"))
    print conn.recvline()
    exit()

while True:
    solve()
"""
key = find_hex(k)
conn.sendline(common_pre+h1+str(i))
print conn.recvline()
print conn.recvline()
"""
