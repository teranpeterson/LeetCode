# SOLVED

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.result

    def helper(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        leftDepth = self.helper(node.left)
        rightDepth = self.helper(node.right)
        if leftDepth + rightDepth > self.result:
            self.result = leftDepth + rightDepth
        return max(leftDepth, rightDepth) + 1

s = Solution()

tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3)) 
print(s.diameterOfBinaryTree(tree))