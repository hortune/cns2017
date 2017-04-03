from pwn import *
import signal
import sys
import os
import time
import base64
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import hlextend

def checkIntegrity(message):
    sha256 = SHA256.new()
    sha256.update(message)
    return base64.b64encode(sha256.digest())

def breakitman(num):
    conn = remote('140.112.31.109',10003)
    time.sleep(5)
    conn.sendline("admin||2||"+checkIntegrity("admin||2"))
    conn.recvuntil('string to me: ')
    mac = conn.recvline()
    conn2 = remote('140.112.31.109',10003)
    time.sleep(5)
    conn2.sendline("admin||"+mac.split("||")[0]+"||"+checkIntegrity("admin||"+mac.split("||")[0]))
    conn2.recvuntil('string to me: ')

    payload = base64.b64decode(conn2.recvline().split('||')[1]).encode("hex")
    origin_mess = "admin"+"||"+mac.split("||")[0]+"||login"
    GG = hlextend.new('sha256')
    padding = GG.extend("||printflag",origin_mess,num,payload,raw=True)
    print padding
    conn.sendline(base64.b64encode(padding)+"||"+base64.b64encode(GG.hexdigest().decode("hex")))
    conn2.close()
    conn.recvline()
    if "error" in conn.recvline():
        conn.close()
        return False
    else:
        print num
        print conn.recvline()
        conn.close()
        exit()
        return True
for i in range(3,250):
    breakitman(i)
