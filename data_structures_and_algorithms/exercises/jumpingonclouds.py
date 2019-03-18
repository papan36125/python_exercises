#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    num_of_jumps=0
    start=0
    current=start
    end=len(c)-1
    while current<end:
        if c[current]!=0:
            current+=1
            continue
        if current!=end-1:
            if c[current+2]==0:
                num_of_jumps +=1
                current+=2
                continue
        if c[current+1]==0:
            num_of_jumps +=1
            current+=1
    return num_of_jumps

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
