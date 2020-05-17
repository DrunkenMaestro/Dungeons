#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count=0
    orange_count=0
    appList=[]
    oList=[]
    for app in apples:
        appList.append(a+app)
    for orr in oranges:
        oList.append(b+orr)
    for i in appList:
        if s<=i<=t:
            apple_count+=1
    for j in oList:
        if s<=j<=t:
            orange_count+=1
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
