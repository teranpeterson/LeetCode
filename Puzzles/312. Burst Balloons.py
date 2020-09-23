# WORKING

import random

class Solution:
    def maxCoins(self, nums):
        n = len(nums)
        nums.append(1)
        while n > 0:
            x = random.randint(0,n-1)
            del nums[x]
            n -= 1
        print(nums)
 
pas = [
    [3,1,5,8],      # 167
]
s = Solution()
for p in pas:
    print("Solution: " + str(s.maxCoins(p)))
