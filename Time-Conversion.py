#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    stamp=''
    timeList = s.split(":")
    hh = int(timeList[0])
    notation = timeList[2][2:]

    if notation=='PM':
        if hh<12:
            hh+=12
            stamp = str(hh)+':'+timeList[1]+':'+timeList[2][0:2]  
        elif hh==12:
            stamp = str(hh)+':'+timeList[1]+':'+timeList[2][0:2]
    
    if notation=='AM':
        if 10>=hh<12 :
            stamp =str(hh)+':'+timeList[1]+':'+timeList[2][0:2]
        if hh<10:
            stamp = '0'+str(hh)+':'+timeList[1]+':'+timeList[2][0:2]
        if hh == 12:
            stamp = '00'+':'+timeList[1]+':'+timeList[2][0:2]
    return stamp
                    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
