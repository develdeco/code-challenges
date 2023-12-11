# Found in code signal
def solution(arr):
    res = ''
    for i in range(len(max(arr,key=len))):
        for word in arr:
            if i < len(word):
                res += word[i]
    return res