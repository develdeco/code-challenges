#!/bin/python3

import os

def freqQuery(queries):
    nums = {}
    freqs = {}
    res = []
    
    for q in queries:
        if q[0] == 1:
            nums[q[1]] = nums.get(q[1], 0) + 1
            freqs[nums[q[1]]] = freqs.get(nums[q[1]], 0) + 1
            if nums[q[1]] > 1:
                freqs[nums[q[1]]-1] -= 1
        elif q[0] == 2 and q[1] in nums:
            nums[q[1]] -= 1
            freqs[nums[q[1]]+1] -= 1
            if nums[q[1]] > 0:
                freqs[nums[q[1]]] += 1
            else:
                del nums[q[1]]
        elif q[0] == 3:
            if q[1] in freqs and freqs[q[1]] > 0:
                res.append(1)
            else:
                res.append(0)
    
    return res
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))
    ans = freqQuery(queries)
    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')
    fptr.close()