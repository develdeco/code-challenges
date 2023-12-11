#!/bin/python3

import os

def luckBalance(k, c, n):
    I = []
    L = 0
    
    for i in range(n):
        if c[i][1] == 0:
            L += c[i][0]
        else:
            I.append(c[i][0])
            
    l = len(I)
    I.sort()
    if k > l: k = l
    for i in range(l-k):
        L -= I[i]
    for i in range(l-k,l):
        L += I[i]
    
    return L

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    contests = []
    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests, n)
    fptr.write(str(result) + '\n')
    fptr.close()