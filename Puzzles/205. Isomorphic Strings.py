# SOLVED

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s
# can be replaced to get t.

# All occurrences of a character must be replaced with another
# character while preserving the order of characters. No two
# characters may map to the same character, but a character
# may map to itself.

# Example 1:
# Input: s = "egg", t = "add"
# Output: true

# Explanation:
# The strings s and t can be made identical by:
# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.

# Example 2:
# Input: s = "f11", t = "b23"
# Output: false

# Explanation:
# The strings s and t can not be made identical as '1' needs
# to be mapped to both '2' and '3'.

# Example 3:
# Input: s = "paper", t = "title"
# Output: true

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        used = {}

        n = ""
        for idx in range(len(s)):
            c = s[idx]
            d = t[idx]

            if c not in m:
                if d in used:
                    return False
                m[c] = d
                used[d] = True
            n += m[c]

        if n == t:
            return True
        else:
            return False

s = Solution()
print(s.isIsomorphic("egg", "add")) # true
print(s.isIsomorphic("f11", "b23")) # false
print(s.isIsomorphic("paper", "title")) # true
print(s.isIsomorphic("badc", "baba")) # false
