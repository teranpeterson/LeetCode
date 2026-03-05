# SOLVED

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
# Return the minimum number of operations needed to make s alternating.

# Example 1:

# Input: s = "0100"
# Output: 1
# Explanation: If you change the last character to '1', s will be "0101", which is alternating.
# Example 2:

# Input: s = "10"
# Output: 0
# Explanation: s is already alternating.
# Example 3:

# Input: s = "1111"
# Output: 2
# Explanation: You need two operations to reach "0101" or "1010".

# Intuition: alternating string must start with a 1 or a 0 and everything else falls into place

class Solution:
    def minOperations(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        
        def opp(x: str):
            if x == "1":
                return "0"
            return "1"

        s0 = 0
        prev = s[0]
        for curr in s[1:]:
            if prev != curr:
                prev = curr
            else:
                s0 += 1
                prev = opp(curr)

        s1 = 1
        prev = opp(s[0])
        for curr in s[1:]:
            if prev != curr:
                prev = curr
            else:
                s1 += 1
                prev = opp(curr)
        
        return min(s0, s1)
            
        

s = Solution()
print(s.minOperations("0100") == 1)
print(s.minOperations("10") == 0)
print(s.minOperations("1111") == 2)
print(s.minOperations("10010100") == 3)
