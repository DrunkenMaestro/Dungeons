#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    # gradeStr=[]
    # finalGrades=[]
    # for i in grades:
    #     gradeStr.append(str(i))
    # for i in gradeStr:
    #     if int(i)>=38:
    #         if int(i[1])<5:
    #             if ((int(i[0])*10) + 5) - int(i) <3:
    #                 finalGrades.append((int(i[0])*10) + 5)
    #             else:
    #                 finalGrades.append((i))
    #         elif int(i[1])>5:
    #             if ((int(i[0])+1)*10) - int(i) <3:
    #                 finalGrades.append((int(i[0])+1)*10)
    #             else:
    #                 finalGrades.append(int(i))
    #         else:
    #             finalGrades.append(int(i))
    #     else:
    #         finalGrades.append(int(i))
    
    # return finalGrades
    x=[]
    for i in grades:
        if i<38 or i%5<3:
            x.append(i)
        else:
            x.append((i-(i%5))+5)
    return x

            


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
