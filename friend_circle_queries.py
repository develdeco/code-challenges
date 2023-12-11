#!/bin/python3

import os

def maxCircle(queries):
    groups, lgroups, numbers = {}, {}, {}
    maxlen = 2
    gnumc = 1
    result = []
    for q in queries:
        if q[0] not in numbers and q[1] not in numbers:
            numbers[q[0]], numbers[q[1]] = gnumc, gnumc
            groups[gnumc] = [q[0],q[1]]
            lgroups[gnumc] = 2
            gnumc += 1
        elif q[0] not in numbers or q[1] not in numbers:
            if q[0] in numbers: num1, num2 = q[0], q[1]
            else: num1, num2 = q[1], q[0]
            gnum = numbers[num1]
            numbers[num2] = gnum
            groups[gnum].append(num2)
            lgroups[gnum] += 1
            if lgroups[gnum] > maxlen: maxlen = lgroups[gnum]
        else:
            gnum1, gnum2 = numbers[q[0]], numbers[q[1]]
            if gnum1 != gnum2:
                if max(lgroups[gnum1],lgroups[gnum2]) == lgroups[gnum2]:
                    gnum1, gnum2 = gnum2, gnum1
                groups[gnum1].extend(groups[gnum2])
                lgroups[gnum1] += lgroups[gnum2]
                if lgroups[gnum1] > maxlen: maxlen = lgroups[gnum1]
                for num in groups[gnum2]: numbers[num] = gnum1
                del groups[gnum2]
                del lgroups[gnum2]
        result.append(maxlen)
    return result
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = maxCircle(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()
