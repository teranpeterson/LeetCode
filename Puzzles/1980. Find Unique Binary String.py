# SOLVED

# Given an array of strings nums containing n unique binary strings each of length n, return
# a binary string of length n that does not appear in nums. If there are multiple answers,
# you may return any of them.

# Example 1:

# Input: nums = ["01","10"]
# Output: "11"
# Explanation: "11" does not appear in nums. "00" would also be correct.
# Example 2:

# Input: nums = ["00","01"]
# Output: "11"
# Explanation: "11" does not appear in nums. "10" would also be correct.
# Example 3:

# Input: nums = ["111","011","001"]
# Output: "101"
# Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

# The n constraint is powerful. We could check n+1 ints and find an answer. Binary conversion + range can do this

from typing import List

class Trie:
    def __init__(self):
        self.zero = None
        self.one = None

    def visit(self, bit: str):
        if bit == "0":
            if not self.zero:
                self.zero = Trie()
            return self.zero
        elif bit == "1":
            if not self.one:
                self.one = Trie()
            return self.one
        else:
            exit(1)
    
    def check(self, path: str) -> bool:
        tree = self
        for p in path:
            if not tree:
                return False
            if p == "0":
                tree = tree.zero
            elif p == "1":
                tree = tree.one
            else:
                exit(1)
        if tree:
            return True
        return False

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        trie = Trie()
        for num in nums:
            step = trie
            for n in num:
                step = step.visit(n)

        return self.generate(trie, len(nums))
    
    def generate(self, tree, depth) -> str:
        if depth == 0:
            return
        if not tree.zero:
            return "0" * depth
        if not tree.one:
            return "1" * depth
        l = self.generate(tree.zero, depth - 1)
        r = self.generate(tree.one, depth - 1)
        if l:
            return "0" + l
        if r:
            return "1" + r

s = Solution()
print(s.findDifferentBinaryString(["01","10"]))
print(s.findDifferentBinaryString(["00","01"]))
print(s.findDifferentBinaryString(["111","011","001"]))
