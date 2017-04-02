#!/usr/bin/env python
import hashlib
import os
import random
import signal
import sys
import time
def sha1(content):
    Hash=hashlib.sha1()
    Hash.update(content)
    return Hash.digest()

def find_hex(string):
    i = 0
    while True:
        UserHash=sha1(str(i)).encode("hex")
        if UserHash[-6:] == "{:0>6}".format(string):
            break 
        i+=1
    return UserHash,i
