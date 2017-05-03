from urlparse import parse_qs
from base64 import b64encode
from base64 import b64decode
from re import match
from Crypto.Cipher import AES
from pwn import *

username = "bals"
password = "gg3be"

conn = remote('140.112.31.109',10004)
conn.sendline('0')
conn.sendline(username)
conn.sendline(password)
conn.recvuntil('token: ')
token = b64decode(conn.recvall().strip())
#

conn.close()
# pt = 'login=' + name + '&role=user' + '&pwd=' +pwd

conn = remote('140.112.31.109',10004)
conn.sendline('0')
conn.sendline('balsnbalsn'+'admin')
conn.sendline(password)
conn.recvuntil('token: ')
token1 = b64decode(conn.recvall().strip())
conn.close()
# 

finaly_token=b64encode(token[:16]+token1[16:])

conn = remote('140.112.31.109',10004)
conn.sendline('1')
conn.sendline(finaly_token)
conn.sendline(username)
conn.sendline(password)
conn.interactive()

#conn.recvuntil('Hi admin:')

conn.close()
