import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    num=s.count('a')*(n//len(s))
    if n%len(s)!=0:
        num += s[:n%len(s)].count('a')
    return num

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')
