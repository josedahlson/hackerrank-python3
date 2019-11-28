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
    new_list = []
    for num in grades:
        if 37 < num < 101:
            if (num + 1) % 5 == 0:
                new_list.append(num + 1)
            elif (num + 2) % 5 == 0:
                new_list.append(num + 2)
            else:
                new_list.append(num)
        elif num < 37:
            new_list.append(num)
    return new_list

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
