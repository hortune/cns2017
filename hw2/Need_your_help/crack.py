# coding: utf-8
priv1  = "".join(open('key.pem','r').readlines()[1:-1]).replace('\n','').replace('-','x').decode("base64").encode("hex")

print priv1
