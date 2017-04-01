import numpy as np
m1 = 'stronger criteria and hence are no longer of'
c1 = 'sgridcelrteia e o rrt h nnoo eaeaogfncrnnr e'
c2 = 'atptaopnpenm lenroghxdooaxdrn etufit edcr n n csiita'

def solve_p6(c1,m1,c2):
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
    print  "".join(sol.T.flatten().tolist()[:-(fence_size-mod)])
    
solve_p6(c1,m1,c2)
