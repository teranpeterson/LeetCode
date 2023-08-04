from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = defaultdict(lambda: 0)
        for m in magazine:
            d[m] += 1
        for n in ransomNote:
            if d[n] > 0:
                d[n] -= 1
            else:
                return False
        return True

s = Solution()
print(s.canConstruct("a", "b") == False)
print(s.canConstruct("aa", "ab") == False)
print(s.canConstruct("aa", "aab") == True)