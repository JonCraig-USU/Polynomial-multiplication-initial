import math
import random

from polyMul import polySchool, poly3, poly4
from nimTime import showTime


sizes = [2**5, 2**6, 2**7, 2**8, 2**9]

def empiricalSchool(n):
    arr0 = [0] * n
    arr1 = [0] * n
    arr2 = [0] * n
    arr3 = [0] * n
    arr4 = [0] * n
    arr5 = [0] * n
    arr6 = [0] * n
    arr7 = [0] * n
    arr8 = [0] * n
    arr9 = [0] * n
    arrays = [arr0, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]
    for i in range (0, n-1):
        for j in arrays:
            j[i] = random.random()
    
    for polyA in arrays:
        for polyB in arrays:
            polySchool(polyA, polyB)


def empirical4(n):
    arr0 = [0] * n
    arr1 = [0] * n
    arr2 = [0] * n
    arr3 = [0] * n
    arr4 = [0] * n
    arr5 = [0] * n
    arr6 = [0] * n
    arr7 = [0] * n
    arr8 = [0] * n
    arr9 = [0] * n
    arrays = [arr0, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]
    for i in range (0, n-1):
        for j in arrays:
            j[i] = random.random()
    
    for polyA in arrays:
        for polyB in arrays:
            poly4(polyA, polyB)
    
def empirical3(n):
    arr0 = [0] * n
    arr1 = [0] * n
    arr2 = [0] * n
    arr3 = [0] * n
    arr4 = [0] * n
    arr5 = [0] * n
    arr6 = [0] * n
    arr7 = [0] * n
    arr8 = [0] * n
    arr9 = [0] * n
    arrays = [arr0, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9]
    for i in range (0, n-1):
        for j in arrays:
            j[i] = random.random()
    
    for polyA in arrays:
        for polyB in arrays:
            poly3(polyA, polyB)
 

showTime(empiricalSchool, sizes)
showTime(empirical4, sizes)
showTime(empirical3, sizes)
