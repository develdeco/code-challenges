#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

def initialize(s):
    # This function is called once before all queries.
    pass
#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def isPalindrome(s, n):
    if n == 1:
        return True
    
    l = int(n//2)
    for i in range(l):
        if s[i] != s[n-1-i]:
            return False
        
    return True

def answerQuery(l, r):
    # Return the answer for this query modulo 1000000007.
    maxLen = 1
    lens = {}
    pals = {}
    chunk = s[l-1:r]
    slen = r-l+1
    
    for i in range(slen):
        word = chunk[i-maxLen+2:i+1]
        for j in range(maxLen-1,i+1):
            word = chunk[i-j] + word
            wlen = j+1
            isPal = True
            if word not in pals:
                isPal = False
                if isPalindrome(word,wlen):
                    pals[word] = 1
                    isPal = True
            if isPal:        
                lens[wlen] = lens.get(wlen,0)+1
                if wlen > maxLen:
                    maxLen = wlen
    
    return lens[maxLen]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        fptr.write(str(result) + '\n')

    fptr.close()
