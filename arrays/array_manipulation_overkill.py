#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

class Zone:
  data = None
  Next = None

def arrayManipulation(n, queries):
    # Write your code here
    maxVal = queries[0][2]
    head = Zone()
    head.Next = Zone()
    head.Next.data = [queries[0][0],queries[0][1],queries[0][2]]
    
    for ix in range(1,len(queries)):
        op = [queries[ix][0],queries[ix][1],queries[ix][2]]
        prev = head
        cur = head.Next
        while cur.Next != None and op[0] > cur.data[1]:
            prev = cur
            cur = cur.Next
            
        if cur.data[1] < op[0]:
            cur.Next = Zone()
            cur.Next.data = op
            if op[2] > maxVal:
                maxVal = op[2]
        else:
            val = None
            while op != None:
                if op[1] < cur.data[0]:
                    new = Zone()
                    new.data = op
                    prev.Next = new
                    new.Next = cur
                    val = op[2]
                else:
                    if cur.data[0] < op[0]:
                        left = Zone()
                        left.data = [cur.data[0],op[0]-1,cur.data[2]]
                        cur.data[0] = op[0]
                        prev.Next = left
                        left.Next = cur
                    if op[1] < cur.data[1]:
                        right = Zone()
                        right.data = [op[1]+1,cur.data[1],cur.data[2]]
                        cur.data[1] = op[1]
                        right.Next = cur.Next
                        cur.Next = right
                    if op[0] < cur.data[0]:
                        left = Zone()
                        left.data = [op[0],cur.data[0]-1,op[2]]
                        prev.Next = left
                        left.Next = cur
                    if cur.data[1] < op[1]:
                        if cur.Next == None:
                            right = Zone()
                            right.data = [cur.data[1]+1,op[1],op[2]]
                            cur.Next = right
                            cur.data[2] += op[2]
                            val = cur.data[2]
                            op = None
                        else:
                            cur.data[2] += op[2]
                            val = cur.data[2]
                            op = [cur.data[1]+1,op[1],op[2]]
                            prev = cur
                            cur = cur.Next
                    else:
                        cur.data[2] += op[2]
                        val = cur.data[2]
                        op = None
                    
                if val > maxVal:
                    maxVal = val
            
    return maxVal

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
