#!/bin/python3

import os

def commonChild(s1, s2):
    b = 0
    m = len(s1)
    n = len(s2)
    e = 0
    
    #trim off the matching items at the beginning
    while b < m and b < n and s1[b] == s2[b]:
        b += 1
        e += 1
        
    #trim off the matching items at the end
    while b < m and b < n and s1[m-1] == s2[n-1]:
        m -= 1
        n -= 1
        e += 1
        
    M = [[0 for _ in range(n-b+1)] for _ in range(m-b+1)]

    for i in range(b,m):
        for j in range(b,n):
            if s1[i] == s2[j]:
                M[i-b+1][j-b+1] = M[i-b][j-b] + 1
            else:
                M[i-b+1][j-b+1] = max(M[i-b+1][j-b], M[i-b][j-b+1])
                
    return M[m-b][n-b] + e

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s1 = input()
    s2 = input()
    result = commonChild(s1, s2)
    fptr.write(str(result) + '\n')
    fptr.close()