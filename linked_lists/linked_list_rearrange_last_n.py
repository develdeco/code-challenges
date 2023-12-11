# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, n):
    if n == 0: return l
    cur = l
    size = 0
    while cur != None:
        size += 1
        cur = cur.next
    cur = l
    tail = None
    for _ in range(size-n):
        tail = cur
        cur = cur.next
    if tail != None:
        prev = None
        while cur != None:
            prev = cur
            cur = cur.next
        prev.next = l
        l = tail.next
        tail.next = None
    return l