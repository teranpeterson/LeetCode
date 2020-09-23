# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        self.n = {}
        self.m = {}
        self.recurse(root, 0)
        print(self.n)
        print(self.m)
        ret = []
        for k in self.m:
            x = self.m[k] / self.n[k]
            ret.append(x)
        return ret

    def recurse(self, node: TreeNode, level: int):
        if node is None:
            return
        if level not in self.n:
            self.n[level] = 0
        if level not in self.m:
            self.m[level] = 0
        self.n[level] += 1
        self.m[level] += node.val
        self.recurse(node.left, level + 1)
        self.recurse(node.right, level + 1)

right = TreeNode(20)
right.left = TreeNode(15)
right.right = TreeNode(7)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = right

print(Solution().averageOfLevels(root))


#     3
#    / \
#   9  20
#     /  \
#    15   7
# [3, 14.5, 11]