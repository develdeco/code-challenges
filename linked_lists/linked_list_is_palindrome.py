# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    head = l
    tail = ListNode(-1)
    
    while head != tail and tail.next != head:
        cur = head
        prev = head
        tail.next = None
        
        while cur.next != None:
            prev = cur
            cur = cur.next
        
        if head.value != cur.value:
            return False
        
        head = head.next
        tail = prev
        
    return True