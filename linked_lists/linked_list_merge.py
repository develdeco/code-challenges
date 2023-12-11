# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l1, l2):
    aux = []
    cur = l1
    while cur != None:
        aux.append(cur.value)
        cur = cur.next
    cur = l2
    while cur != None:
        aux.append(cur.value)
        cur = cur.next
    head = None
    nxt = None
    for num in sorted(aux, reverse=True):
        head = ListNode(num)
        head.next = nxt
        nxt = head
    return head