#!/bin/python3

import os

def getMinimumCost(k, c, n):
    cost = 0
    c.sort()
    for i in range(n):
        mult = (i // k) + 1
        cost += mult * c[n-1-i]
    return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c, n)
    fptr.write(str(minimumCost) + '\n')
    fptr.close()