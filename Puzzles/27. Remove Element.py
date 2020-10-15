# SOLVED

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) < 1:
            return 0
        begin = 0
        end = len(nums)
        while begin != end:
            if nums[begin] == val:
                end -= 1
                nums[begin], nums[end] = nums[end], nums[begin]
            else:
                begin += 1
        return len(nums[:end])

print(Solution().removeElement([1], 1))