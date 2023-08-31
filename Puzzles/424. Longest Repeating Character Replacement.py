# SOLVED

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = defaultdict(lambda: 0)
        l, r = 0, 0
        maxF = 0
        res = 0
        while r < len(s):
            c = s[r]
            hashMap[c] += 1
            maxF = max(maxF, hashMap[c])

            if (r - l + 1) - maxF <= k:
                res = max(res, r - l + 1)
            else:
                while (r - l + 1) - maxF > k:
                    hashMap[s[l]] -= 1
                    l += 1
            r += 1
        return res
            


s = Solution()
print(s.characterReplacement("ABAB", 2) == 4)
print(s.characterReplacement("AABABBA", 1) == 4)
print(s.characterReplacement("AAAA", 0) == 4)
