#!/usr/bin/python
import signal
import sys
import os
import time

from base64 import b64encode
from base64 import b64decode
from Crypto.Cipher import AES

import secret
FLAG = secret.FLAG
KEY = secret.KEY
IV = secret.IV

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[-1])]

def check_pad(s):

    if(len(s) % 16 != 0):
        return False

    N = ord(s[-1])
    if(N > 16 or N < 1):
        return False

    padding = s[-N:]
    if(padding != N * chr(N)):
        return False
    return True

def AES_encrypt(m):

    global IV, KEY

    m = pad(m)
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    return b64encode(aes.encrypt(m))

def alarm(time):
    def handler(signum, frame):
        print 'Timeout. Bye~Bye~'
        exit()
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(time)

def encrypt_flag():

    global FLAG

    print 'Encrypted FLAG:'
    print AES_encrypt(FLAG)

def can_you_decrypt():

    global IV, KEY

    print 'Can you decrypt it?'
    for i in range(948794):

        s = raw_input().strip()
        try:
            s = b64decode(s)
            if(len(s) == 0):
                break
            elif(len(s) < 16):
                print 'ValueError: IV must be 16 bytes long'

            iv = s[:16]
            cipher = s[16:]

            aes = AES.new(KEY, AES.MODE_CBC, iv)
            plain = aes.decrypt(cipher)
            if(check_pad(plain) == True):
                decrypt_flag = unpad(plain)
                print 'success.'
            else:
                print 'fail.'
        except:
            print 'fail.'


def main():

    time.sleep(1)
    alarm(60)

    encrypt_flag()
    can_you_decrypt()


if __name__ == '__main__':

    sys.dont_write_bytecode = True
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
    sys.stdin = os.fdopen(sys.stdin.fileno(), 'r', 0)

    main()
