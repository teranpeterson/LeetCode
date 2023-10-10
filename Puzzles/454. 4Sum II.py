# SOLVED

from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        n = len(nums1)
        m = defaultdict(lambda: 0)
        for three in nums3:
            for four in nums4:
                m[three + four] += 1

        for i in range(n):
            for j in range(n):
                count += m[0 - (nums1[i] + nums2[j])]
        
        return count


s = Solution()
print(s.fourSumCount([1,2], [-2,-1], [-1,2], [0,2])) # 2
print(s.fourSumCount([0], [0], [0], [0])) # 1