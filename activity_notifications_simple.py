#!/bin/python3

import os

def activityNotifications(exp, d, n):
    notes = 0
    mod = d % 2
    mpos = int(d//2) + mod
    for i in range(d,n):
        t = exp[i-d:i]
        t.sort()
        if mod > 0:
            med = t[mpos-1]
        else:
            med = (t[mpos-1] + t[mpos]) / 2
        if exp[i] >= 2*med:
            notes += 1
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