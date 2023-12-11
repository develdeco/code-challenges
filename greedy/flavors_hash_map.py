#!/bin/python3

def whatFlavors(cost, money):
    diff = {}
    for i, c in enumerate(cost,1):
        if c in diff:
            print(diff[c],i)
            return
        diff[money-c] = i

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
