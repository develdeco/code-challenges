#!/bin/python3

import os

def countTriplets(arr, r):
    count = 0
    second = {}
    third = {}

    for x in arr:
        nxt = x*r

        if x in third:
            count += third[x]

        if x in second:
            third[nxt] = third.get(nxt, 0) + second[x]

        second[nxt] = second.get(nxt, 0) + 1
        
    return count
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    fptr.write(str(ans) + '\n')
    fptr.close()