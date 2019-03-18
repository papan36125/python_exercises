import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
	arr = [0] * (n+1)
	max = 0
	for i in range(len(queries)):
		a=queries[i][0]
		b=queries[i][1]
		k=queries[i][2]
		arr[a] += k
		if b+1 <=n:
			arr[b+1] -=k
	temp = 0
	for i in range(n+1):
		temp += arr[i]
		if temp > max:
			max = temp
		
	return max

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')