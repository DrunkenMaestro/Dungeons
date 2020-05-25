#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    resultant = dict()
    yList=[]
    for i in range (len(p)):
        resultant[i+1]= p[i]
    for x in range(1, len(p)+1):
        for y in p:
            if resultant[resultant[y]]==x:
                yList.append(y)

    return yList


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
