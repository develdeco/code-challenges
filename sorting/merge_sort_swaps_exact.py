#!/bin/python3

import os

def merge(arr, begin, mid, end):
    l = begin
    r = mid+1
    i = 0
    n = end-begin+1
    laux = [0] * n
    needed = mid-l+1
    swaps = 0
    
    while l <= mid and r <= end:
        if arr[l] <= arr[r]:
            laux[i] = arr[l]
            l += 1
            needed -= 1
        else:
            laux[i] = arr[r]
            r += 1
            swaps += needed
        i += 1
    
    while l <= mid:
        laux[i] = arr[l]
        l += 1
        i += 1
        
    while r <= end:
        laux[i] = arr[r]
        r += 1
        i += 1
        
    while i > 0:
        arr[end+1-i] = laux[n-i]
        i -= 1
        
    return swaps

def mergeSort(arr, begin, end):
    if begin < end:
        mid = int((end+begin+1)//2)-1
        l = mergeSort(arr, begin, mid)
        r = mergeSort(arr, mid+1, end)
        c = merge(arr, begin, mid, end)
        return l + r + c
    else:
        return 0

def countInversions(arr, n):
    return mergeSort(arr, 0, n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = countInversions(arr, n)
        fptr.write(str(result) + '\n')
    fptr.close()