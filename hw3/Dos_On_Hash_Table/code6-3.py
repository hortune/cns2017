print (32768)
threshold = 2**30
lastbig = 0
for i in range(0,1073709056+1,32768):
	if i <= threshold:
		lastbig = i
		print(i)
	else :
		print(lastbig)

