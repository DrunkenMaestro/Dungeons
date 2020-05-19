#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    sCount=0
    ar.append('extra')
    i=0
    while(i<n):
        if ar[i]==ar[i+1]:
            sCount+=1
            i+=2
        else:
            i+=1
            
    return sCount


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
