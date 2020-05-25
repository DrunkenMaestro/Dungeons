#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    beautiful=0
    for day in range(i,j+1):
        if abs(day - reverseDay(day))%k==0:
            beautiful+=1
    return beautiful

def reverseDay(num):
    if str(num)[:-1]!=0:         #Checking if last digit is 0
        return int(str(num)[::-1])
    else:
        length = str(num)
        return int(str(num)[(length-1)::-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
