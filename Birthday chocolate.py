#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(s, d, m):
    tCount=0
    month=m
    start=0
    while month<=len(s):
        if sum(s[start:month])==d:
            tCount+=1
        start+=1
        month+=1
    return tCount

    # tCount=0
    # x=0
    # tsum=0
    # if m<=len(s):
    #     for i in range(len(s)):
    #         x=i+m
    #         if x<=len(s):
    #             for j in range(i,x):
    #                 tsum+=s[j]
    #                 print(tsum)
    #                 if (tsum==d):
    #                     tCount+=1
    #                     tsum=0
    # return tCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
