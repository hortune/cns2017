# coding: utf-8
from pwn import *
import hashlib

p = 262603487816194488181258352326988232210376591996146252542919605878805005469693782312718749915099841408908446760404481236646436295067318626356598442952156854984209550714670817589388406059285064542905718710475775121565983586780136825600264380868770029680925618588391997934473191054590812256197806034618157751903
"""
for iter1 in range(1,21):
    for iter2 in range(1,21):
        for iter3 in range(1,21):
"""          
            
def guess(iter1,iter2,iter3):   
    print "now", iter1,iter2,iter3
    num_to_send = [iter1,iter2,iter3]
    num_to_send = [int(hashlib.sha512(str(i)).hexdigest(),16) for i in num_to_send]
    g = [pow(i,2,p) for i in num_to_send]
    conn = remote('140.112.31.109',10002)
    conn.recvuntil('Server sends: ')
    b0 = int(conn.recvline().strip())
    #print "b0",b0 
    conn.sendline(str(g[0]))
   
    
    conn.recvuntil('Server sends: ')
    b1 = int(conn.recvline().strip())
    conn.sendline(str(g[1]))
    #print "b1", b1
                
    conn.recvuntil('Server sends: ')
    b2 = int(conn.recvline().strip())
    #print "b2", b2
    conn.sendline(str(g[2]))
   
    conn.recvuntil('FLAG is: ')
    cipher = int(conn.recvline().strip())
    #print "cipher", cipher
    print cipher
    b = [b0,b1,b2]
    
    for keys in b:
        cipher ^= int(hashlib.sha512(str(keys)).hexdigest(), 16)
    
    print (cipher)
    flag = "{0:x}".format(cipher)
    print (flag)
    if len(flag)%2==0:
        flag = flag.decode("hex")
        if "BALSN" in flag:
            print flag
            exit()
        print flag

    conn.close()

