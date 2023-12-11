#!/bin/python3

import os

def flippingBits(n):
    l = 32
    b2 = [0] * l
    pos = l-1
    c = n
    
    while c > 1:
        m = c % 2
        c = c // 2
        b2[pos] = m
        pos -= 1
    b2[pos] = c
    
    r = 0
    for i in range(l):
        b = -1*b2[i]+1
        r += pow(2,l-1-i)*b
    
    return r
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()