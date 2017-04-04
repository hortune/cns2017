from pwn import *
import numpy as np
def solve_p6(conn):
    conn.recvuntil("m1 = ")
    m1 = conn.recvline()
    conn.recvuntil("c1 = ")
    c1 = conn.recvline()
    conn.recvuntil("c2 = ")
    c2 = conn.recvline()
    conn.recvuntil("=")
    
    c2 = c2[:-1]

    print c1
    print c2
    print m1
    fence_size =  m1.find(c1[1])
    m2 = list(c2)
    le = len(c2)
    mod = le%fence_size
    le -= mod
    side = le/fence_size
    sol = []
    for i in range(mod):
        sol.append(m2[:side+1])
        m2 = m2[side+1:]

    for i in range(mod,fence_size):
        sol.append(m2[:side]+['.'])
        m2 = m2[side:]
    
    sol = np.array(sol)
    print "".join(sol.T.flatten().tolist()[:-(fence_size-mod)])
    
    return conn
def solve_p5(conn):
    
    conn.recvuntil("m1 = ")
    m1 = conn.recvline()
    conn.recvuntil("c1 = ")
    c1 = conn.recvline()
    conn.recvuntil("c2 = ")
    c2 = conn.recvline()
    conn.recvuntil("=")
    m2 = list(c2)
    dic = {}
    for i in range(len(c1)):
        m2[m1.find(c1[i])] = c2[i]
    ans = "".join(m2)
    if ans[-1] == '\n':
        ans = ans[:-1]
    conn.sendline(ans)
    return conn
def solve_p3(conn):
    conn.recvuntil("m1 = ")
    m1 = conn.recvline()
    conn.recvuntil("c1 = ")
    c1 = conn.recvline()
    conn.recvuntil("c2 = ")
    c2 = conn.recvline()
    conn.recvuntil("=")
    
    m2=""
    delta = ord(m1[0])-ord(c1[0])
    for i in c2:
        if i in ' \n':
            m2+=i
        elif i.islower():
            m2 +=chr((delta+26+ord(i)-ord('a'))%26+ord('a'))
        else:
            m2 +=chr((delta+26+ord(i)-ord('A'))%26+ord('A'))
        delta -=1
    #conn.sendline(m2)
    if m2[-1] == '\n':
        m2 = m2[:-1]
    
    conn.sendline(m2)
    return conn


def solver(c1,m1,c2,delta = 6666):
    m2 = ""
    if delta == 6666:
       delta = ord(m1[0])-ord(c1[0])
    for i in c2:
        if i in ' \n':
            m2 += i
            continue
        if i.islower():
            new_ascii = ((delta+ord(i)-ord('a'))+26)%26+ord('a')
            m2 = m2 + chr(new_ascii)
        else:
            new_ascii = ((delta+ord(i)-ord('A'))+26)%26+ord('A')
            m2 = m2 + chr(new_ascii)
    return m2

def solve_p4(conn):
    conn.recvuntil("m1 = ")
    m1 = conn.recvline()
    conn.recvuntil("c1 = ")
    c1 = conn.recvline()
    conn.recvuntil("c2 = ")
    c2 = conn.recvline()
    conn.recvuntil("=")
    
    c1 = c1.replace(' ','')
    m1 = m1.replace(' ','')
    keys = [(ord(i)-ord(j)+26)%26 for i,j in zip(m1,c1)]
    for i in range(4,len(keys)):
        if keys[i:i+4] == keys[:4]:
            keys = keys[:i]
            break
    initial  = 0 
    ans = ""
    for s in c2[:-1]:
        if  s == ' ':
            ans = ans + s
        elif s.islower():
            ans += chr((ord(s) + keys[(initial)%len(keys)] -ord('a'))%26 + ord('a'))
            initial += 1
        else:
            ans += chr((ord(s) + keys[(initial)%len(keys)] -ord('A'))%26 + ord('A'))
            initial +=1
    print ans
    if ans[-1] == '\n':
        ans = ans[:-1]
    conn.sendline(ans) 
    return conn
def solve_345(conn):
    conn = solve_p3(conn)
    conn = solve_p4(conn)
    conn = solve_p5(conn)
    return conn

conn = remote('140.112.31.109',10000)
conn.recvuntil(' = ')
m1 = conn.recvline()
conn.recvuntil(' = ')
c1 = conn.recvline()

conn.recvuntil(' = ')
c2 = conn.recvline()

conn.recvuntil(' = ')
m2 = solver(c1,m1,c2)
conn.send(m2)

conn.recvuntil(' = ')
c2 = conn.recvline()

for i in range(26):
    print(solver(c1,m1,c2,i))


