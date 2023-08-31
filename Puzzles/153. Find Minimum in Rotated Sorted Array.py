# SOLVED

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            half = l + (r - l) // 2
            if nums[l] < nums[half] and nums[r] < nums[half]:
                l = half
            elif nums[l] > nums[half] and nums[r] > nums[half]:
                r = half
            elif nums[l] < nums[half]:
                r = half - 1
            elif nums[r] < nums[half]:
                l = half + 1
            else:
                r = half - 1

        return nums[l]

s = Solution()
print(s.findMin([3,4,5,1,2]) == 1)
print(s.findMin([4,5,6,7,0,1,2]) == 0)
print(s.findMin([11,13,15,17]) == 11)
print(s.findMin([2,1]) == 1)
print(s.findMin([3,1,2]) == 1)
