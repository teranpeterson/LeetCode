# SOLVED

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            k = i + (j - i) // 2
            n = nums[k]
            if n > target:
                j = k - 1
            elif n < target:
                i = k + 1
            else:
                return k
        return -1


s = Solution()
print(s.search([-1,0,3,5,9,12], 9) == 4)
print(s.search([-1,0,3,5,9,12], 2) == -1)
print(s.search([5], 5) == 0)