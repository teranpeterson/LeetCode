class Solution:
    def maxSubArray(self, nums):
        ret = 0
        if not nums:
            return ret
        start = 0
        while True:
            end = 0
            prev = 0

        



pas = [
    [-2,1,-3,4,-1,2,1,-5,4],
]

s = Solution()
for p in pas:
    print(s.maxSubArray(p))