#!/bin/python3

import sys

sys.setrecursionlimit(15000)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def serializeTree(root):
    if not root:
        return []
    arr = serializeTree(root.left)
    arr.append(root.data)
    arr.extend(serializeTree(root.right))
    return arr
    
def printTree(root):
    print(' '.join(map(str,serializeTree(root))))

def swapAtDepth(root, depth):
    if not root:
        return
    if depth > 1:
        swapAtDepth(root.left, depth-1)
        swapAtDepth(root.right, depth-1)
    else:
        aux = root.left
        root.left = root.right
        root.right = aux

def swapNodes(indexes, queries):
    root = Node(1)
    nodes = [root]
    pos = 0
    depth = 0
    
    while pos < len(indexes):
        aux = []
        for node in nodes:
            ix = indexes[pos]
            if ix[0] > 0:
                node.left = Node(ix[0])
                aux.append(node.left)
            if ix[1] > 0:
                node.right = Node(ix[1])
                aux.append(node.right)
            pos += 1
        nodes = aux
        depth += 1
        
    result = []
    for q in queries:
        k = q
        while k < depth:
            swapAtDepth(root, k)
            k += q
        result.append(serializeTree(root))
    
    return result

if __name__ == '__main__':
    fptr = open('tree_swap_nodes.txt', 'w')
    n = int(input().strip())
    indexes = []
    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)
    result = swapNodes(indexes, queries)
    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')
    fptr.close()