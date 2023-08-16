# SOLVED

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root: Optional[TreeNode]):
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(left - right) > 1:
                res = False
            return max(left, right) + 1
        
        dfs(root)
        return res

s = Solution()

tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(s.isBalanced(tree) == True)

tree = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print(s.isBalanced(tree) == False)