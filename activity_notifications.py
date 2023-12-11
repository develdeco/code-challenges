#!/bin/python3

import os

def activityNotifications(exp, d, n):
    notes = 0
    mod = d % 2
    mpos = int(d//2) + mod
    carr = [0] * (201)
    
    for i in range(d):
        carr[exp[i]] += 1
    
    for i in range(d,n):
        pos = 0
        ix = 0
        while pos <= mpos-1:
            med = ix
            pos += carr[ix]
            ix += 1
        
        if mod == 0 and pos <= mpos:
            while pos <= mpos:
                med2 = ix
                pos += carr[ix]
                ix += 1
            med = (med+med2)/2
            
        if exp[i] >= 2*med:
            notes += 1
            
        carr[exp[i-d]] -= 1
        carr[exp[i]] += 1
            
    return notes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d, n)
    fptr.write(str(result) + '\n')
    fptr.close()