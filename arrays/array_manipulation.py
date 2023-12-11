#!/bin/python3

import os

class Zone:
  data = None
  Next = None

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0] * (n+1)
    for op in queries:
        arr[op[0]] += op[2]
        if op[1]+1 <= n:
            arr[op[1]+1] -= op[2]
        
    val = 0
    maxVal = 0
    for x in arr:
        val += x
        if val > maxVal:
            maxVal = val
            
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    queries = []
    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))
    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()