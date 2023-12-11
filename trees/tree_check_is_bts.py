""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
    
def checkLeft(node, val):
    if node == None:
        return True
    if node.data < val:
        return checkLeft(node.left, val) and checkLeft(node.right, val)
    else:
        return False

def checkRight(node, val):
    if node == None:
        return True
    if node.data > val:
        return checkRight(node.left, val) and checkRight(node.right, val)
    else:
        return False
    
data = {} 
def checkBST(root):
    if root.data in data:
        return False
    else:
        data[root.data] = None
    if root.left == None and root.right == None:
        return True
    if root.left == None:
        return checkBST(root.right) and checkRight(root.right, root.data)
    if root.right == None:
        return checkBST(root.left) and checkLeft(root.left, root.data)
    if not checkBST(root.left) or not checkBST(root.right):
        return False
    if not checkLeft(root.left, root.data) or not checkRight(root.right, root.data):
        return False
    return True
    