#!/bin/python3

def maxSubsetSum(arr):
    l = len(arr)
    if l == 1: return arr[0]
    dp = [arr[0],max(arr[0],arr[1])]
    for i in range(2,l):
        dp.append(max(arr[i],dp[i-2],dp[i-1],dp[i-2]+arr[i]))
    return max(dp[l-1],0)

if __name__ == '__main__':
    fptr = open('dp_max_array_sum.txt', 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    fptr.write(str(res) + '\n')
    fptr.close()
