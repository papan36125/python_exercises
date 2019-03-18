#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    sea_level =0
    count_valley = 0
    for step in s:
        if step == 'U':
            sea_level +=1
        if step == 'D':
            sea_level -=1
        if step == 'U' and sea_level == 0:
            count_valley +=1
    return count_valley

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')
