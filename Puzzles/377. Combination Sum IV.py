# WORKING

class Solution:
    def combinationSum4(self, nums, target):
        ret = 0
        l = len(nums)-1
        i = l
        j = l
        while i >= 0 and j >= 0:
            x = nums[i] + nums[j]
            print("x=" + str(x))
            if x > target:
                j -= 1
            if x < target:
                pass
            if x == target:
                ret += 1
                j -= 1
            if j < 0:
                i -= 1
                j = l
        return ret

nums = [1, 2, 3]
target = 4
# 7

s = Solution()
print("Solution: " + str(s.combinationSum4(nums, target)))