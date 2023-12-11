class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def solution(a, b):
    cura, sa = a, []
    curb, sb = b, []
    while cura != None:
        sa.append(cura.value)
        cura = cura.next
    while curb != None:
        sb.append(curb.value)
        curb = curb.next
    nxt = None
    head = None
    n = max(len(sa),len(sb))
    leftover = 0
    sa.reverse()
    sb.reverse()
    for i in range(n):
        numa, numb = 0, 0
        if i < len(sa): numa = sa[i]
        if i < len(sb): numb = sb[i]
        sumval = numa + numb + leftover
        if sumval > 9999:
            s = str(sumval)
            leftover = int(s[:len(s)-4])
            sumval = int(s[len(s)-4:])
        else: leftover = 0
        head = ListNode(sumval)
        head.next = nxt
        nxt = head
    if leftover > 0:
        head = ListNode(leftover)
        head.next = nxt
    return head