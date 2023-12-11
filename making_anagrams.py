#!/bin/python3

import os

def makeAnagram(a, b):
    ab1 = [0] * 26
    ab2 = [0] * 26
    apos = ord('a')
    
    for l in a:
        ab1[ord(l)-apos] += 1
        
    for l in b:
        ab2[ord(l)-apos] += 1
        
    dels = 0
    for i in range(26):
        dels += abs(ab1[i]-ab2[i])
        
    return dels

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()