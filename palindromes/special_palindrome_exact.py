#!/bin/python3

import math
import os
import random
import re
import sys

def isPalindrome(s, n):
    if n == 1:
        return True
    
    l = int(n//2)
    for i in range(l):
        if s[i] != s[n-1-i]:
            return False
        if i > 0 and s[i-1] != s[i]:
            return False
        
    return True

# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    pals = {}
    for i in range(n):
        word = ''
        for j in range(i+1):
            word = s[i-j] + word
            isPal = True
            if word not in pals:
                isPal = False
                if isPalindrome(word, j+1):
                    pals[word] = 1
                    isPal = True
            if isPal:
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
