#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    vCount=0
    step=0
    for i in range(n):
        if s[i]=='U':
            step+=1
            if step==0:
                vCount+=1
        else:
            step-=1
        
    return vCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
