# coding: utf-8

"""
Getting Data
"""
parameters = [ i.rstrip().split() for i in open('parameters')]
parameters = [ i for i in parameters if len(i)]
parameters = [ int(i[2]) for i in parameters if len(i)]
p,g,a,b,cipher = parameters
"""        
Since g_backdoor = g^((n-1)/691829)  restrict the range by fermet theorem
"""
mul = g
power_num =0
for i in range(1,691829):
    mul %= p
    if mul == a:
        power_num = i
        break
    mul *= g

"""
get the small num a
"""

s = pow(b,power_num,p)

"""
implement eucliden algorithm
"""

def xgcd(b, n):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while n != 0:
                q, b, n = b // n, n, b % n
                x0, x1 = x1, x0 - q * x1
                y0, y1 = y1, y0 - q * y1
        return  b, x0, y0
    
flag = xgcd(s,p)[1]
flag = flag * cipher 
flag %= p
print "{0:x}".format(flag).decode("hex")
