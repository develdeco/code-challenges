#!/bin/python3

import os

def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))
    
    ans = 0
    apos, bpos, cpos = len(a)-1, len(b)-1, len(c)-1
    while bpos >= 0 and b[bpos] >= a[0] and b[bpos] >= c[0]:
        while apos >= 0 and b[bpos] < a[apos]:
            apos -= 1
            
        while cpos >= 0 and b[bpos] < c[cpos]:
            cpos -= 1    
            
        ans += (apos+1) * (cpos+1)
        bpos -= 1
            
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    lenl = input().split()
    lena, lenb, lenc = int(lenl[0]), int(lenl[1]), int(lenl[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    fptr.write(str(ans) + '\n')
    fptr.close()
