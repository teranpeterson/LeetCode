# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root):
        self.sum = 0
        self.recurse(root, "")
        return self.sum

    def recurse(self, node, s):
        if not node:
            return
        s += str(node.val)
        if not node.left and not node.right:
            self.sum += int(s, 2)
            return
        self.recurse(node.left, s)
        self.recurse(node.right, s)


x = TreeNode(1)
l = TreeNode(0)
l.left = TreeNode(0)
l.right = TreeNode(1)
r = TreeNode(1)
r.left = TreeNode(0)
r.right = TreeNode(1)
x.left = l
x.right = r


s = Solution()
print("Solution: " + str(s.sumRootToLeaf(x)))


#   0
# 1   1
#  2 1 1