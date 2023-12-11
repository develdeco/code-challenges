# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l, k):
    head = l
    while head != None and head.value == k:
        head = head.next
        
    prev = head
    cur = head
    while cur != None:
        if cur.value == k:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    
    return head