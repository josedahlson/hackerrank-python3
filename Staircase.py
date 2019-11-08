#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for count in range(1, n+1):
        print(" " * (n - count) + "#" * count)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
