#!/bin/python3

import os

def maxXor(arr, queries):
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2 
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in '{:b}'.format(n).zfill(k):
            tmp = str(int(char) ^ 1) 
            tmp, c = (tmp, '1') if tmp in node else (char, '0')
            s += c 
            node = node[tmp]
        ans.append(int(s, 2))
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    queries = []
    for _ in range(m):
        queries_item = int(input())
        queries.append(queries_item)
    result = maxXor(arr, queries)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
