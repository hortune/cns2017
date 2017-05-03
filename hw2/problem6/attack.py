from pwn import *
ans= "".join(open('ca.crt','r').readlines()).encode('base64').replace('\n','')
conn = remote('140.112.31.109',10005)
conn.sendline(ans)
conn.interactive()
