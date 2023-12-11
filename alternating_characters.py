#!/bin/python3

import os

def alternatingCharacters(s):
    checker = 0
    dels = 0
    abvals = {'A': 1,'B': -1}
    for l in s:
        checker += abvals[l]
        if abs(checker) > 1:
            dels += 1
            checker -= abvals[l]
        elif checker == 0:
            checker += abvals[l]
    return dels
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    for q_itr in range(q):
        s = input()
        result = alternatingCharacters(s)
        fptr.write(str(result) + '\n')
    fptr.close()