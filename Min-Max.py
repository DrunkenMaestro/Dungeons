#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    mini =arr[0]
    maxi =arr[0]
    miniSum=0
    maxiSum=0
    if (sum(arr)!=arr[0]*5):
        for val in arr:
            if min(mini,val)<mini:
                mini = min(mini,val)
            if max(maxi,val)>maxi:
                maxi = max(maxi,val)
        for val in arr:
    
            if val == maxi:
                continue
            miniSum+=val
              
    
        for val in arr:
            if val==mini:
                continue
            maxiSum+=val
    
        print(str(miniSum)+' '+str(maxiSum))
    else:
        print(str(arr[0]*4)+' '+str(arr[0]*4))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
