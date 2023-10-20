# SOLVED

from typing import List

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for num in nums:
            res = res & set(num)
        return list(res)

s = Solution()
print(s.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(s.intersection([[1,2,3],[4,5,6]]))