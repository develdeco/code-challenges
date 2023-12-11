#!/bin/python3

import os

def highestValuePalindrome(s, n, k):
    if n == 1:
        if s[0] == '9' or k > 0:
            return '9'
        else:
            return str(-1)
    
    l = int(n//2)
    swaps = [2] * l
    for i in range(l):
        if s[i] != s[n-1-i]:
            if k == 0:
                return str(-1)
            
            if int(s[i]) > int(s[n-1-i]):
                s = s[:n-1-i] + s[i] + s[n-i:]
            else:
                s = s[:i] + s[n-1-i] + s[i+1:]
                
            k -= 1
            swaps[i] -= 1
        
    for i in range(l):
        if s[i] != '9' and k >= swaps[i]:
            s = s[:i] + '9' + s[i+1:n-1-i] + '9' + s[n-i:]
            k -= swaps[i]
        
        if k == 0:
            return s
        
    if n-l > l and k > 0:
        s = s[:l] + '9' + s[n-l:]

    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = input()
    result = highestValuePalindrome(s, n, k)
    fptr.write(result + '\n')
    fptr.close()