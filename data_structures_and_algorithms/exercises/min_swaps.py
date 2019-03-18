#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    i=0
    map = {}
    sorted_arr = sorted(arr)
    for j in range(len(arr)):
        map[arr[j]] = j
    while i < len(arr):

        if arr[i] == sorted_arr[i]:
            i+=1
            continue
        idx = map[sorted_arr[i]]
        map[arr[i]] = map[sorted_arr[i]]
        arr[i],arr[idx] = sorted_arr[i],arr[i]
        swaps +=1
        i +=1
    return swaps


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res) + '\n')
