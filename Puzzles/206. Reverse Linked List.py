# SOLVED

from collections import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Recursive
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def recur(prev, curr):
            if not curr:
                return prev
            next = curr.next
            curr.next = prev
            return recur(curr, next)
        return recur(None, head)

    # Iterative
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev = None
    #     curr = head
    #     while True:
    #         if not curr:
    #             break
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #     return prev

s = Solution()
