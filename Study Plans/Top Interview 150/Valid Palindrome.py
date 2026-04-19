# SOLVED

# Regex is overkill, use isalnum()

# A phrase is a palindrome if, after converting all
# uppercase letters into lowercase letters and removing
# all non-alphanumeric characters, it reads the same
# forward and backward. Alphanumeric characters include
# letters and numbers.

# Given a string s, return true if it is a palindrome,
# or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing
# non-alphanumeric characters.
# Since an empty string reads the same forward and
# backward, it is a palindrome.

import re

valid_char = r'[a-z0-9]'

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            l_c = s[l].lower()
            r_c = s[r].lower()
            if not re.search(valid_char, l_c):
                l += 1
                continue
            if not re.search(valid_char, r_c):
                r -= 1
                continue
            if l_c != r_c:
                return False
            l += 1
            r -= 1
        return True

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama") == True)
print(s.isPalindrome("race a car") == False)
print(s.isPalindrome(" ") == True)
print(s.isPalindrome("0P") == False)
