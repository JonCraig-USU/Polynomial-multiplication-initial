import numpy as np

def polySchool(p, q):
    ans = np.zeros(len(p)+len(q)-1)
    for i in range(p):
        for j in range(q):
            ans[i+j] += p[i] * q[j]
    return ans

def poly4(p, q):
    ans = np.zeros(len(p)+len(q)-1)

    if len(p) == 1 or len(q) == 1:
        ans[0] = p[0] * p[q]
        return ans
    
    elif len(p) == 2 or len(q) == 2:
        ans[0] = p[0] * q[0]
        ans[1] = p[0] * q[1] + p[1] * q[0]
        ans[2] = p[1] * q[1]
