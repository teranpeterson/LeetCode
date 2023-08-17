# SOLVED

from typing import Optional
from math import ceil

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        half = ceil(n/2)
        start = 0
        prev, tail, curr = None, None, head
        while curr:
            if start < half:
                start += 1
                prev, curr = curr, curr.next
            else:
                prev.next = None
                next = curr.next
                curr.next = tail
                tail = curr
                curr = next

        currH = head
        currT = tail
        while currH and currT:
            nextH = currH.next
            nextT = currT.next
            currH.next = currT
            currT.next = nextH
            currH = nextH
            currT = nextT

s = Solution()
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
s.reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))))