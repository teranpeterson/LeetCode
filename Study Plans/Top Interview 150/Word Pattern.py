# SOLVED

# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection
# between a letter in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the
# same letter.

# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true

# Explanation:
# The bijection can be established as:
# 'a' maps to "dog".
# 'b' maps to "cat".

# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false

# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        m = {}
        used = {}

        words = s.split(' ')

        if len(pattern) != len(words):
            return False

        for idx in range(len(pattern)):
            letter = pattern[idx]
            word = words[idx]
            if letter in m:
                if m[letter] == word:
                    continue
                else:
                    return False
            else:
                if word in used:
                    return False
                else:
                    m[letter] = word
                    used[word] = True
        return True

s = Solution()
print(s.wordPattern("abba", "dog cat cat dog")) # true
print(s.wordPattern("abba", "dog cat cat fish")) # false
print(s.wordPattern("aaaa", "dog cat cat dog")) # false
print(s.wordPattern("abba", "dog dog dog dog")) # false
print(s.wordPattern("aaa", "aa aa aa aa")) # false
