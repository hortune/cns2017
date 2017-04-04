# coding: utf-8
from pwn import *
import hashlib
import time

p = 262603487816194488181258352326988232210376591996146252542919605878805005469693782312718749915099841408908446760404481236646436295067318626356598442952156854984209550714670817589388406059285064542905718710475775121565983586780136825600264380868770029680925618588391997934473191054590812256197806034618157751903
            
nsd = [str(pow(int(hashlib.sha512(str(i)).hexdigest(),16),2,p)) for i in range(21)]

def guess(num):
    for index in range(1,21):
        conn = remote('140.112.31.109',10002)
        conn1 = remote('140.112.31.109',10002)
        for qq in range(3): 
            if qq == num:
                conn.recvuntil('Server sends: ')
                b = int(conn.recvline().strip())
                conn.sendline(nsd[index])
                
                conn1.recvuntil('Server sends: ')
                b1 = int(conn1.recvline().strip())
                conn1.sendline(nsd[index])
            else:
                conn.recvuntil('Server sends: ')
                conn1.recvuntil('Server sends: ')
                temp = int(conn.recvline().strip())
                temp1 = int(conn1.recvline().strip())
                conn.sendline(str(temp1))
                conn1.sendline(str(temp))
        conn.recvuntil('FLAG is: ')
        cipher = int(conn.recvline().strip())
        conn1.recvuntil('FLAG is: ')
        cipher1 = int(conn1.recvline().strip())
        
        conn.close()
        conn1.close()
        b = int(hashlib.sha512(str(b)).hexdigest(),16)
        b1 = int(hashlib.sha512(str(b1)).hexdigest(),16)
        if cipher^cipher1^b^b1 == 0:
            return index
def sol(iter1,iter2,iter3):   
    print "now", iter1,iter2,iter3
    conn = remote('140.112.31.109',10002)
    conn.recvuntil('Server sends: ')
    b0 = int(conn.recvline().strip())
    conn.sendline(nsd[iter1])
    conn.recvuntil('Server sends: ')
    b1 = int(conn.recvline().strip())
    conn.sendline(nsd[iter2])
    conn.recvuntil('Server sends: ')
    b2 = int(conn.recvline().strip())
    conn.sendline(nsd[iter3])
    conn.recvuntil('FLAG is: ')
    cipher = int(conn.recvline().strip())
    b = [b0,b1,b2]
    for keys in b:
        cipher ^= int(hashlib.sha512(str(keys)).hexdigest(), 16)
    flag = "{0:x}".format(cipher)
    if len(flag)%2==0:
        flag = flag.decode("hex")
        if "BALSN" in flag:
            print flag
            exit()
    conn.close()
sol(guess(0),guess(1),guess(2))
