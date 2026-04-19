# SOLVED

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than
# ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.


# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(lambda: 0)
        target = len(nums) / 2

        for num in nums:
            m[num] += 1
            if m[num] > target:
                return num

s = Solution()
print(s.majorityElement([3,2,3])) # 3
print(s.majorityElement([2,2,1,1,1,2,2])) # 2
