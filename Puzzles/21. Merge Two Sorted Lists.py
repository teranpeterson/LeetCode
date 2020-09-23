# SOLVED

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        ret = ListNode("x")
        nxt = ret
        while l1 != None or l2 != None:
            if l1 == None:
                nxt.next = ListNode(l2.val)
                l2 = l2.next
            elif l2 == None:
                nxt.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                nxt.next = ListNode(l1.val)
                l1 = l1.next
            elif l2.val < l1.val:
                nxt.next = ListNode(l2.val)
                l2 = l2.next
            else:
                nxt.next = ListNode(l1.val)
                l1 = l1.next
            nxt = nxt.next
        return ret.next


a = ListNode(1)
b = ListNode(2)
c = ListNode(4)

b.next = c
a.next = b

e = ListNode(1)
f = ListNode(3)
g = ListNode(4)

f.next = g
e.next = f

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

s = Solution()
x = s.mergeTwoLists(a, e)
while x != None:
    print(x.val)
    x = x.next