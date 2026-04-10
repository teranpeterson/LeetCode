# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order, and each of their
# nodes contains a single digit. Add the two numbers and return the sum
# as a linked list.

# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = l1
        n2 = l2

        head = ListNode(0)

        curr = head
        carry = 0
        while n1 or n2:
            node = ListNode(0)
            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0
            x = v1 + v2 + carry
            node.val = x % 10
            carry = x // 10
            curr.next = node

            curr = curr.next
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        
        if carry > 0:
            node = ListNode(1)
            curr.next = node
        
        return head.next


s = Solution()

l1_a = ListNode(9)
l1_b = ListNode(9, l1_a)
l1_c = ListNode(9, l1_b)
l1_d = ListNode(9, l1_c)
l1_e = ListNode(9, l1_d)
l1_f = ListNode(9, l1_e)
l1_g = ListNode(9, l1_f)

l2_a = ListNode(9)
l2_b = ListNode(9, l2_a)
l2_c = ListNode(9, l2_b)
l2_d = ListNode(9, l2_c)



x = s.addTwoNumbers(l1_g, l2_d)
while x:
    print(x.val)
    x = x.next
