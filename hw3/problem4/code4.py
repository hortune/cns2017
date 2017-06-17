from pwn import *
from base64 import b64decode, b64encode
from IPython import embed

def create_commit(pre_cipher,manipulate,target):
	return b64encode(pre_cipher + manipulate + target)

def attack_cipher_block(conn, ciphers):
	target = ciphers[-1]
	manipulate = list(ciphers[-2])
	after_cipher = [0] * 16
	ans = [0]*16
	pre_cipher = "".join(ciphers[:-2])
			

	for i in range(15,-1,-1):
		# take pre_answer to fullfil cipher
		for gg in range(15,i,-1):
			manipulate[gg] = chr(ord(after_cipher[gg])^(16-i))
		#embed()
		for char in range(256):
			manipulate[i] = chr(char)
			#manipulate[i] = chr(224)
			padd = create_commit(pre_cipher,"".join(manipulate),target)
			conn.sendline(padd)
			mes = conn.readuntil('.')
			#print(i,char,mes)
			if char == 224:
				continue
			if 'success' in mes:
				after_cipher[i] = chr(char ^ (16 - i))
				#print(ord(ciphers[-2][i]),16-i,char)
				ans[i] = chr(char ^ (16 - i) ^ ord(ciphers[-2][i]))
				#print(ans[i])
				break
	return "".join(ans)
		 
			

cipher = b64decode("eK6+EJRrtcTDgo5d8OYF2tf20dWQ4BQ1ZU0FnnpjEozGPJNVZHDFWpo9dMgEcYddEi5xGZAYLYPVx0H8dtPR4CfBbl5wmPbRFqF+1k+HBXc=")
conn = connect('140.112.31.109',10006)
conn.readuntil('Can you decrypt it?\n')

ciphers = [cipher[i*16:(i+1)*16] for i in range(5)]

answers = [0]*5

for i in range(5,2,-1):
	answers[i-1] = attack_cipher_block(conn,ciphers[:i])
	#print(i,answers[i-1])
conn.close()
conn = connect('140.112.31.109',10006)
conn.readuntil('Can you decrypt it?\n')
for i in range(2,1,-1):
	answers[i-1] = attack_cipher_block(conn,ciphers[:i])
	#print(i,answers[i-1])
print "BALSN{"+"".join(answers[1:])	
