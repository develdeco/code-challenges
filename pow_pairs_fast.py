# Found in code signal
def isPowTwo(n):
    return n != 0 and (n & (n-1) == 0)

def solution(a):
    n = len(a)
    pairs = 0
    for i in range(n):
        for j in range(i,n):
            if isPowTwo(a[i]+a[j]):
                pairs += 1
    return pairs