#!/bin/python3

import os

def maxMin(k, arr, n):
    arr.sort()
    res = arr[n-1]-arr[n-k]
    for i in range(n-k+1):
        diff = arr[n-1-i]-arr[n-i-k]
        if diff < res:
            res = diff
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = maxMin(k, arr, n)
    fptr.write(str(result) + '\n')
    fptr.close()