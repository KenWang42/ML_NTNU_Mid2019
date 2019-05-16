import math
import random
import itertools

lst1 = [-4,-5,-2,-8,-7,4]
lst2 = [-3,10,-9,-3,6,9]
lst3 = [-2,10,-6,-5,-5]

comlst1 = list(itertools.combinations(lst1, 3))


def splitListEven(lst):
    comlst = []
    if (len(lst) % 2 == 0):
        size = int(len(lst) / 2)
        comlst = list(itertools.combinations(lst, size))
        print(comlst)
    min = float('inf')
    comlstR = []
    comlstL = []
    for sublst in comlst:
        sumlst = list(sum(sublst))
        print(sumlst)
    return (comlstR, comlstL)


splitListEven(lst1)