#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    # fCount=0
    # bCount=0
    # i=1
    # while(i<=n):
    #     if i!=p :
    #         fCount+=1
    #         i+=1
    #     else:
    #         break
    # while(n>=1):
    #     if n!=p :
    #         bCount+=1
    #         n-=1
    #     else:
    #         break
    # print(fCount,bCount)
    # return min(fCount,bCount)
    return min(p//2,n//2-p//2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
