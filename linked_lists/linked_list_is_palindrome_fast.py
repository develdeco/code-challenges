# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def solution(l):
    cur = l
    aux = []
    while cur != None:
       aux.append(cur.value)
       cur = cur.next
    n = len(aux)//2
    return len(aux) == 1 or aux[:n] == aux[::-1][:n]