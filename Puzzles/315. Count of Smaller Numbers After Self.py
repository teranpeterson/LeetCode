# WORKING

class Solution:
    def countSmaller(self, nums):
        l = len(nums)
        lst = [0] * l
        for i in range(l-1, -1, -1):
            n = nums[i]
            for j in range(i-1, -1, -1):
                m = nums[j]
                if n < m:
                    lst[j] += 1
        return lst

pas = [
    [5,2,6,1],      # [2,1,1,0]
]
s = Solution()
for p in pas:
    print("Solution: " + str(s.countSmaller(p)))
