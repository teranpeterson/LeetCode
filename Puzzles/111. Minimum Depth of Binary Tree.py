# WORKING

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        self.min = float('inf')
        self.minDepthHelper(root, 1)
        return self.min

        
    def minDepthHelper(self, node, depth):
        if depth > self.min:
            return
        if node == None:
            if depth-1 < self.min:
                self.min = depth - 1
            return
        self.minDepthHelper(node.left, depth + 1)
        self.minDepthHelper(node.right, depth + 1)
    

x = TreeNode(20)
x.left = TreeNode(15)
x.right = TreeNode(7)

a = TreeNode(3)
a.left = TreeNode(9)
a.right = x

a = TreeNode(1)
a.left = TreeNode(2)


s = Solution()
print("Solution: " + str(s.minDepth(a)))