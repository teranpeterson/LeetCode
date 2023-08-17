# SOLVED

from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(lambda: 0)
        maxL = 0

        l, r = 0, 0

        while r < len(s):
            hashmap[s[r]] += 1

            while hashmap[s[r]] > 1:
                hashmap[s[l]] -= 1
                l += 1

            r += 1
            maxL = max(maxL, r - l)
        
        return maxL
            

            

s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb") == 3)
print(s.lengthOfLongestSubstring("bbbbb") == 1)
print(s.lengthOfLongestSubstring("pwwkew") == 3)
print(s.lengthOfLongestSubstring("dvdf") == 3)


# pwwkew

# p = 0
# w = 2
# k = 0
# e = 0