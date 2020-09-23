# SOLVED

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        if Counter(s) == Counter(t):
            return True
        else:
            return False


pas = [

]
s = Solution()
for p in pas:
    print("Solution: " + str(s.isAnagram(p)))