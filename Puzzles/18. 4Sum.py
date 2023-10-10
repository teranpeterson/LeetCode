# SOLVED

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        nums.sort()

        for i in range(len(nums)):
            n = nums[i]
            if i > 0 and nums[i - 1] == n:
                continue
            for j in range(i + 1, len(nums)):
                m = nums[j]
                if j > i + 1 and nums[j - 1] == m:
                    continue

                l, r = j + 1, len(nums) - 1
                while l < r:
                    k = nums[l]
                    p = nums[r]
                    if n + m + k + p < target:
                        l += 1
                    elif n + m + k + p > target:
                        r -= 1
                    else:
                        result.append([n, m, k, p])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1

        return result

s = Solution()
print(s.fourSum([1,0,-1,0,-2,2], 0))
print(s.fourSum([2,2,2,2,2], 8))