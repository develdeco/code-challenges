# Found in code signal
def solution(s, t):
    res = 0
    for i in range(len(max([s,t],key=len))):
        if i < len(s) and s[i].isdigit() and s[:i]+s[i+1:] < t:
            res += 1
        if i < len(t) and t[i].isdigit() and s < t[:i]+t[i+1:]:
            res += 1
    return res