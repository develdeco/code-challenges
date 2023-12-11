#!/bin/python3

def equal(arr):
    n = max(arr)
    C = [0]*(n+1)
    S = [0]*(n+1)
    pos, ans = n, 0
    
    for i in arr:
        C[i] += 1
        if i < pos:
            pos = i
    
    while pos < n:
        diff = 1
        pos += 1
        while C[pos] == 0:
            diff += 1
            pos += 1
        
        S[pos] = C[pos-diff]+1
        C[pos] -= 1

        if C[pos] > 0 or pos < n:
            C.extend([0]*diff)
            S.extend([0]*diff)
        
            for i in range(pos,n+1):
                if i+diff > n:
                    C[i+diff] = C[i]
                else:
                    S[i+diff] = C[i]
                C[i] = S[i]
                S[i] = 0
            
            n += diff
    
        for i in [5,2,1]:
            ans += diff//i
            diff = diff%i
    
    return ans

if __name__ == '__main__':
    fptr = open('dp_equal_slow.txt', 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = equal(arr)
        fptr.write(str(result) + '\n')
    fptr.close()