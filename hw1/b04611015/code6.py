import os
import string

messages = [i.rstrip() for i in open('cipher')]

def xor_string(x,y):
    if len(x)>len(y):
        return ''.join([chr(ord(z)^ord(p)) for z,p in zip(x[:len(y)],y)])
    else:
        return ''.join([chr(ord(z)^ord(p)) for z,p in zip(x,y[:len(x)])])

len_array = [len(list(message.decode('hex'))) for message in messages]

rc = []

for i in xrange(min(len_array)):
    t = []
    for current in xrange(256):
        ok = True
        for index in range(len(messages)):
            message = messages[index]
            tmp = list(message.decode('hex'))
            val = current ^ ord(tmp[i])
            if index == 8:
                if chr(val) not in string.lowercase + string.uppercase + " .,{}":
                    ok = False
                    break
            else:
                if chr(val) not in string.lowercase + string.uppercase + " .,":
                    ok = False
                    break

        if ok:
            t.append(current)
    rc.append(t)

print rc
key = []

for pos in rc:
    key.append(pos[0])

def gen():
    _key = ''.join(map(chr,key))
    for i in range(0,len(messages)):
        print xor_string(_key,messages[i].decode('hex'))
key[0]=126
def modify(row,column,target):
    key[column]=ord(messages[row].decode("hex")[column])^ord(target)
