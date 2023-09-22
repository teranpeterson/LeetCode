# WORKING

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                res += maxR - height[r]
        
        return res


s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6)
print(s.trap([4,2,0,3,2,5]) == 9)
print(s.trap([4,2,3]) == 1)

# [0,1,0,2,1,0,1,3,2,1,2,1]
#  0,0,1,1,2,4,5,5,6,8,9,11