# SOLVED

from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l <= r:
            k = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            
            if hours > h:
                l = k + 1
            elif hours <= h:
                r = k - 1
        
        return l


s = Solution()
print(s.minEatingSpeed([3,6,7,11], 8) == 4)
print(s.minEatingSpeed([30,11,23,4,20], 5) == 30)
print(s.minEatingSpeed([30,11,23,4,20], 6) == 23)