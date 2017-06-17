from random import randint

#PERTURB_SHIFT = 5
shift = 1<<17
#N = 100
#for qaq in range(N):
#	print (qaq)


#count = N
#for qaq in range(1,50000000):
se = set([])
sed = []
j = 0
print(50000)
while True:
	print (j+shift)
	sed.append(j)
	if j in se:
		break
	se.add(j)
	if len(se) == 22000:
		break
	
	j = ((5*j) + 1 ) & (shift-1)


for i in range(15000):
	print(1)
	print(0)

#print (shift)
#for i in range(20000):
#	print(0)
