#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    am_pm = s.split(":")
    am_pm_str = am_pm[-1][2:].lower()

    if am_pm_str == "pm":
        am_pm[0] = str(int(am_pm[0]) + 12)
        if am_pm[0] == "24":
            am_pm[0] = "12"
        new_str = ":".join(am_pm)
        return new_str[0:8]
    elif am_pm_str == "am":
        if am_pm[0] == "12":
            am_pm[0] = "00"
        new_str = ":".join(am_pm)
        return new_str[0:8]


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
