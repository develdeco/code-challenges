#!/bin/python3

import os

def minimumSwaps(arr):
    swaps = 0
    rep = list(range(0,len(arr)+1))
    repPos = list(range(0,len(arr)+1))
    pos = len(arr)
    
    while pos > 0:
        if rep[pos] != arr[pos-1]:
            cur = rep[pos]
            new = rep[repPos[arr[pos-1]]]
            rep[pos] = new
            rep[repPos[arr[pos-1]]] = cur
            repPos[cur] = repPos[arr[pos-1]]
            repPos[new] = pos
            swaps += 1
        pos -= 1

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    fptr.write(str(res) + '\n')
    fptr.close()