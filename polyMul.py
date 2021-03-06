import numpy as np
from numpy.lib.function_base import append

def polySchool(p, q):
    ans = np.zeros(len(p)+len(q)-1)
    for i in range(len(p)):
        for j in range(len(q)):
            ans[i+j] += p[i] * q[j]
    return ans

def poly4(p, q):
    l = len(p)  # length of the 2 matrices
    ans = np.zeros(2 * l -1)

    if l == 1:
        ans[0] = p[0] * q[0]
        return ans
    
    elif l == 2:
        ans[0] = p[0] * q[0]
        ans[1] = p[0] * q[1] + p[1] * q[0]
        ans[2] = p[1] * q[1]
        return ans

    else:
        # recurrsive calls for the 4 sub parts 
        low = poly4(p[0:l//2], q[0:l//2])        # low terms are the x**0 indexes to the midway
        middleA = poly4(p[0:l//2], q[l//2:l])   # inside term of foil
        middleB = poly4(p[l//2:l], q[0:l//2])   # insider term of foil
        high = poly4(p[l//2:l], q[l//2:l])     # high terms are the midpoint to the end of the array
        
        # Pad all the arrays so that they match the length of answer
        half = int(l//2)
        low = np.append(low, np.zeros(l))
        middleA = np.append(np.zeros(half), middleA)
        middleA = np.append(middleA, np.zeros(half))
        middleB = np.append(np.zeros(half), middleB)
        middleB = np.append(middleB, np.zeros(half)) 
        high = np.append(np.zeros(l), high)

        # update the answer array
        ans = np.add(ans, low)
        ans = np.add(ans, middleA)
        ans = np.add(ans, middleB)
        ans = np.add(ans, high)

        # return updated array back up the chain
        return ans

# print("===============================================")
# print(polySchool([8, 7, 6, 5], [4, 3, 2, 1]))
# print(poly4([8, 7], [4, 3]))

# print("===============================================")
# print(polySchool([1, 2, 3, 4], [1, 2, 3, 4]))
# print(poly4([1, 2, 3, 4], [1, 2, 3, 4]))


def poly3(p, q):
    l = len(p)
    ans = np.zeros(2 * l - 1)

    if l == 1:
        ans[0] = p[0] * q[0]
        return ans
    
    # else:
    #     a = p[odd]
    #     b = p[even]
    #     c = q[odd]
    #     d = q[even]
    #     inside = poly3(a+b, c+d)
    #     left = poly3(a, c)
    #     right = poly3(b, d)
    #     left = np.add(left, inside)
    #     return np.add(left, right)


