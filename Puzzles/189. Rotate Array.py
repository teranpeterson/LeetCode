# SOLVED

# My cyclic detection code is naive and doesn't fully work.
# Need to utilize GCD for it.

# Given an integer array nums, rotate the array to
# the right by k steps, where k is non-negative.

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

from typing import List

class Solution:
    def rotateReplacement(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = nums[0]
        idx = 0
        even = False
        if len(nums) % 2 == 0 and len(nums) > 2 and k % 2 == 0:
            even = True

        for n in range(len(nums)):
            if even and n == len(nums)/2:
                idx = (idx + 1) % len(nums)
                prev = nums[idx]
            target = (idx + k) % len(nums)
            print(f'{nums} | {prev} -> {target}')

            prev, nums[target] = nums[target], prev
            idx = target
            print(nums)
        return nums
    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(0, len(nums)-1)
        reverse(0, k-1)
        reverse(k, len(nums)-1)
        return nums

        
s = Solution()
print(s.rotate([1,2,3,4,5,6,7], 0) == [1,2,3,4,5,6,7])
print(s.rotate([1,2,3,4,5,6,7], 1) == [7,1,2,3,4,5,6])
print(s.rotate([1,2,3,4,5,6,7], 2) == [6,7,1,2,3,4,5])
print(s.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4])
print(s.rotate([1,2,3,4,5,6,7], 4) == [4,5,6,7,1,2,3])
print(s.rotate([1,2,3,4,5,6,7], 5) == [3,4,5,6,7,1,2])
print(s.rotate([1,2,3,4,5,6,7], 6) == [2,3,4,5,6,7,1])
print(s.rotate([1,2,3,4,5,6,7], 7) == [1,2,3,4,5,6,7])
print(s.rotate([-1,-100,3,99], 0) == [-1,-100,3,99])
print(s.rotate([-1,-100,3,99], 1) == [99,-1,-100,3])
print(s.rotate([-1,-100,3,99], 2) == [3,99,-1,-100])
print(s.rotate([-1,-100,3,99], 3) == [-100,3,99,-1])
print(s.rotate([-1,-100,3,99], 4) == [-1,-100,3,99])
print(s.rotate([1,2], 1) == [2,1])
print(s.rotate([1,2,3,4,5,6], 3) == [4,5,6,1,2,3])
n = [1,2,3,4,5,6]
print(s.rotate(n, 3))
print(n == [4,5,6,1,2,3])
