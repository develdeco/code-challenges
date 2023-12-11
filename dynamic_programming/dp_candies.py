#!/bin/python3

import os

def candies(n, arr):
    C = [1]*n
    ans = n
    
    for i in range(1,n):
        if arr[i-1] < arr[i]:
            ans += C[i-1]
            C[i] = C[i-1]+1
            
    for j in range(2,n+1):
        i = n-j
        if arr[i] > arr[i+1] and C[i] <= C[i+1]:
            ans += C[i+1]-C[i]+1
            C[i] = C[i+1]+1
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)
    result = candies(n, arr)
    fptr.write(str(result) + '\n')
    fptr.close()