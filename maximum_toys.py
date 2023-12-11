#!/bin/python3

import os

def maximumToys(prices, k):
    toys = 0
    spent = 0
    prices.sort()
    for price in prices:
        spent += price
        if spent <= k:
            toys += 1
        else:
            return toys
    return toys
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()