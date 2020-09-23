# SOLVED

class Solution:
    def twoSum(self, nums, target):
        m = {}
        for i in range(len(nums)):
            n = nums[i]
            c = target - n
            if c in m:
                return [m[c], i]
            m[n] = i
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9))
# [2,7,11,15]
# 9
# [0,1]

s = Solution()
print(s.twoSum([2,1,9,4,4,56,90,3], 8))
# [2,1,9,4,4,56,90,3]
# 8
# [3,4]

s = Solution()
print(s.twoSum([3,2,4], 6))
# [3,2,4]
# 6
# [1,2]

s = Solution()
print(s.twoSum([-1,-2,-3,-4,-5], -8))
# [-1,-2,-3,-4,-5]
# -8
# [2,4]

s = Solution()
print(s.twoSum([0,4,3,0], 0))
# [0,4,3,0]
# 0
# [0,3]