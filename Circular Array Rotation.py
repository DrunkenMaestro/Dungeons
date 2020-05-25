#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    # resultList=[]
    # while k!=0:
    #     rotateList=[]
    #     rotateList.append(a[-1])
    #     rotateList += a[0:len(a)-1]
    #     a=rotateList
    #     k-=1
    # for i in queries:
    #     resultList.append(a[i])
    # return resultList
    items = deque(a) 
    items.rotate(k)
    resultList = []
    for q in queries:
        #print(items[q])
        resultList.append(items[q])
    return resultList

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
