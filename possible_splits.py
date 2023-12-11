# Found in code signal
def solution(s):
    n, res = len(s),0
    for i in range(n-2):
        a = s[:i+1]
        for j in range(i+1,n-1):
            b,c = s[i+1:j+1],s[j+1:]
            if len(a) == len(c) or len(b) == len(c):
                if len(a) == len(c) and a+b == b+c: continue
                if len(b) == len(c) and a+b == c+a: continue
            res += 1
    return res

print(solution("xzxzx"))