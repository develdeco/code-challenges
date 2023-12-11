#!/bin/python3

import os

def pairs(k, arr):
    diff = {}
    ans = 0
    for num in arr:
        if num in diff:
           ans += diff[num]
        diff[num+k] = diff.get(num+k,0)+1
        diff[num-k] = diff.get(num-k,0)+1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    fptr.write(str(result) + '\n')
    fptr.close()
