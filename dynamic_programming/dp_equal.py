#!/bin/python3

def equal(arr):
    n = max(arr)
    C = [0]*(n+1)
    pos, ans = n, 0
    
    for i in arr:
        C[i] += 1
        if i < pos:
            pos = i

    for i in range(pos+1,n+1):
        if C[i] > 0:
            diff = i-pos
            count = 0
            for j in [5,2,1]:
                count += diff//j
                diff = diff%j
            count *= C[i]
            ans += count

    return ans

if __name__ == '__main__':
    fptr = open('dp_equal.txt', 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = equal(arr)
        fptr.write(str(result) + '\n')
    fptr.close()