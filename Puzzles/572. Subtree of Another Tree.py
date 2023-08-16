# SOLVED

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], check = False) -> bool:
        if not root and not subRoot:
            return True
        
        if not root and subRoot:
            return False
        
        if root and not subRoot:
            return False
        
        res = False
        if root.val == subRoot.val:
            res = self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True)
        
        if check:
            return res
        
        return res or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


s = Solution()

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(s.isSubtree(root, subRoot) == True)

root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
print(s.isSubtree(root, subRoot) == False)