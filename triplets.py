# Found in code signal
def solution(arr, queries):
    res = []
    for q in queries:
        count = 0
        second = {}
        third = {}
        for x in arr:
            if x in third:
                count += third[x]
            if x in second:
                third[q[2]] = third.get(q[2],0) + second[x]
            if x == q[0]:
                second[q[1]] = second.get(q[1],0) + 1
        res.append(count)
    return res