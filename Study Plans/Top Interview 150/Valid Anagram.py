# SOLVED

# Given two strings s and t, return true if t is an 
# anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False

s = Solution()
print(s.isAnagram("anagram", "nagaram")) # true
print(s.isAnagram("rat", "car")) # false
