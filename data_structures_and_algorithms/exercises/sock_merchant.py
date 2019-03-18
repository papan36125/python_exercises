import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    num_of_pairs = 0
    pair_idx = []
    for i in range(n):
        if i == n-1:
            break
        if i in pair_idx:
            continue
        if ar[i] not in ar[i+1:]:
            continue
        pair_idx.append(i)
        pair_idx.append(ar.index(ar[i], i+1))
        num_of_pairs += 1
    return num_of_pairs

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(str(result))
