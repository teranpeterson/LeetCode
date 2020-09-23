# SOLVED

class Solution:
    def search(self, nums, target):
        if len(nums) < 1:
            return -1
        prev = 0
        if target == nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums)-1
        if target > nums[0]:
            for i in range(len(nums)):
                n = nums[i]
                prev = n
                if n == target:
                    return i
        if target < nums[-1]:
            for i in reversed(range(len(nums))):
                n = nums[i]
                prev = n
                if n == target:
                    return i
        return -1

pas = [
    [4,5,6,7,0,1,2],    # 0

]
s = Solution()
# for p in pas:
print("Solution: " + str(s.search([4,5,6,7,0,1,2], 7)))
