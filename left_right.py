# Found in code signal
def solution(numbers, left, right):
    n = len(numbers)
    res = [False]*n
    for i in range(n):
        if numbers[i]%(i+1) == 0:
            x = numbers[i]//(i+1)
            if left <= x and x <= right:
                res[i] = True
    return res