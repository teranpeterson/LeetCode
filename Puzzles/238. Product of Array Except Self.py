# SOLVED

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            res[i] *= prod
            prod *= nums[i]
        prod = 1
        for j in range(len(nums) - 1, -1, -1):
            res[j] *= prod
            prod *= nums[j]
        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4]) == [24,12,8,6])
print(s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0])