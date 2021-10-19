import numpy as np

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
        ans[0] = p[0] * p[q]
        return ans
    
    elif l == 2:
        ans[0] = p[0] * q[0]
        ans[1] = p[0] * q[1] + p[1] * q[0]
        ans[2] = p[1] * q[1]

    else:
        # recurrsive calls for the 4 sub parts 
        low = poly4(p[:l//2], q[:l//2])        # low terms are the x**0 indexes to the midway
        middleA = poly4(p[:l//2], q[l//2:l])   # inside term of foil
        middleB = poly4(p[l//2:l], q[:l//2])   # insider term of foil
        high = poly4(p[l//2:l], q[l//2:l])     # high terms are the midpoint to the end of the array
        
        # Pad all the arrays so that they match the length of answer
        np.append(low, np.zeros(l))
        np.append(np.zeros(l//2), middleA, np.zeros(l//2))
        np.append(np.zeros(l//2), middleB, np.zeros(l//2)) 
        np.append(np.zeros(l), high)

        # update the answer array
        np.add(ans, low)
        np.add(ans, middleA)
        np.add(ans, middleB)
        np.add(ans, high)

        # return updated array back up the chain
        return ans


print(polySchool([8, 7, 6, 5], [4, 3, 2, 1]))
# x1 = np.arange(9.0).reshape((3, 3))
# print(x1)
# x2 = np.arange(3.0)
# print(x2)
# x3 = x1 + x2
# print(x3)
# print(np.add(x1, x1, x1))
print(poly4([8, 7, 6, 5], [4, 3, 2, 1]))
print(poly4([1, 2, 3, 4], [1, 2, 3, 4]))


