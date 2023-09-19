# SOLVED

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        res = 0
        
        for n in nums:
            if (n - 1) not in m:
                i = 1
                while n + i in m:
                    i += 1
                res = max(res, i)
        
        return res


s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))

# [0,3,7,2,5,8,4,6,0,1]
#    ^
# {0: 1, }