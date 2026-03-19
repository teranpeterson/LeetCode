# SOLVED

# Given an array of positive integers nums and a positive integer target, return
# the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = len(nums)
        found = False
        p0 = 0
        p1 = 1
        curr = sum(nums[p0:p1])
        while p1 <= len(nums):
            if p0 == p1:
                p1 +=1
                continue

            print(f'{nums[p0:p1]} -> {sum(nums[p0:p1])} vs {curr}')
            if curr < target:
                try:
                    curr += nums[p1]
                except:
                    break
                p1 += 1
                if p1 - p0 > res:
                    curr -= nums[p0]
                    p0 += 1
                continue
            else:
                if p1 - p0 <= res:
                    found = True
                    res = p1 - p0
                curr -= nums[p0]
                p0 += 1
        
        if found:
            return res
        return 0

        

s = Solution()
print(s.minSubArrayLen(7, [2,3,1,2,4,3])) # 2
print(s.minSubArrayLen(4, [1,4,4])) # 1
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1])) # 0
print(s.minSubArrayLen(15, [1,2,3,4,5])) # 5
print(s.minSubArrayLen(7, [5])) # 0
