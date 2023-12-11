#!/bin/python3

import os

def countTriplets(arr, r):
    count = 0
    
    if r == 1:
        refs = {}
        for x in arr:
            if x not in refs:
                refs[x] = -1
            else:
                refs[x] += 1
                if refs[x] >= 1:
                    count += int(refs[x]*(refs[x]+1)/2)
    else:
        second = {}
        third = {}
        for x in arr:
            nxt = x*r
            if nxt not in second:
                second[nxt] = 1
            else:
                second[nxt] += 1
            
            if x in second:
                if nxt not in third:
                    third[nxt] = second[x]
                else:
                    third[nxt] += second[x]
            
            if x in third:
                count += third[x]
        
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