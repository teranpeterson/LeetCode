# SOLVED

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []

        nums.sort()

        for k in range(len(nums)):
            a = nums[k]
            if k > 0 and a == nums[k - 1]:
                continue

            l = k + 1
            r = len(nums) - 1
            while l < r:
                b = nums[l]
                c = nums[r]

                total = a + b + c
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    ret.append([a,b,c])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return ret


s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]])
print(s.threeSum([0,1,1]) == [])
print(s.threeSum([0,0,0]) == [[0,0,0]])
print(s.threeSum([0,0,0]) == [[0,0,0]])
print(s.threeSum([0,0,0,0]) == [[0,0,0]])
print(s.threeSum([1,-1,-1,0]) == [[-1,0,1]])

# [-1, 0, 1, 2,-1,-4]
# [-4,-1,-1, 0, 1, 2]