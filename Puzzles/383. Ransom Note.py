# SOLVED

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = Counter(magazine)
        for letter in ransomNote:
            if letter in c and c[letter] > 0:
                c[letter] -= 1
            else:
                return False
        return True

s = Solution()
print(s.canConstruct("a", "b")) # false
print(s.canConstruct("aa", "ab")) # false
print(s.canConstruct("aa", "aab")) # true
