# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    size = 0
    cur = l
    while cur != None:
        size += 1
        cur = cur.next
    if k > size: return l
    head = None
    prev_last = None
    cur = l
    n = size-(size%k)
    for _ in range(0,n,k):
        last = cur
        prev = None
        for _ in range(k):
            aux = cur.next
            cur.next = prev
            prev = cur
            cur = aux
        if prev_last != None: prev_last.next = prev
        else: head = prev
        prev_last = last
    prev_last.next = cur
    return head