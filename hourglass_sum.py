#!/bin/python3

import os

def hourglassSum(arr):
    pattern = [
        (0,1),(0,2),(1,1),(2,0),(2,1),(2,2)
    ]
    sums = [0] * 16
    
    for i in range(0,4):
        for j in range(0,4):
            pos = (i,j)
            sums[i*4+j] += arr[i][j]
            for t in range(0, len(pattern)):
                ppos = tuple(map(sum, zip(pos, pattern[t])))
                sums[i*4+j] += arr[ppos[0]][ppos[1]]
    
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()