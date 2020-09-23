# SOLVED

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        self.print_node(l1)
        self.print_node(l2)
        res = None
        start = None
        carry = 0
        while l1 is not None or l2 is not None:
            n = 0
            m = 0
            if l1 is not None:
                n = l1.val
                l1 = l1.next
            if l2 is not None:
                m = l2.val
                l2 = l2.next
            x = n + m + carry
            if carry == 1:
                carry = 0
            if x > 9:
                carry = 1
                x = x - 10
            new = ListNode(x)
            if res is None:
                res = new
                start = res
            else:
                res.next = new
                res = res.next
        if carry > 0:
            last = ListNode(carry)
            res.next = last
        self.print_node(start)
        return start
    
    def print_node(self, node):
        temp = node
        print(temp.val, end="")
        temp = temp.next
        while temp is not None:
            print(" -> ", end="")
            print(temp.val, end="")
            temp = temp.next
        print()

a1 = ListNode(9)
a2 = ListNode(9)
a3 = ListNode(9)
a2.next = a3
a1.next = a2

b1 = ListNode(9)
b2 = ListNode(9)
b3 = ListNode(9)
b2.next = b3
b1.next = b2

c1 = ListNode(2)
c2 = ListNode(4)
c1.next = c2

d1 = ListNode(2)
d2 = ListNode(4)
d1.next = d2

s = Solution()
s.addTwoNumbers(a1, b1)

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Input: (2 -> 4) + (2 -> 4 -> 2)
# Output: 4 -> 8 -> 2
# Explanation: 42 + 242 = 284.

# Input: (2 -> 4 -> 3) + (2 -> 4)
# Output: 4 -> 8 -> 3
# Explanation: 342 + 42 = 384.

# Input: (9 -> 9 -> 9) + (9 -> 9 -> 9)
# Output: 8 -> 9 -> 9 -> 1
# Explanation: 999 + 999 = 1998.