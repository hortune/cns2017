from random import randint

attack_list = []

N = 100
threshold = 1 << 16
for i in range(N):
	attack_list.append(randint(1,threshold))

for i in range(50000):
	print(attack_list[i%N]+randint(1,2**20)*threshold)

