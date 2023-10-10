# SOLVED

from typing import List
from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        m = defaultdict(lambda: 0)

        for t in time:
            c = t % 60
            count += m[(60 - c) % 60]
            m[c] += 1
        
        return count

s = Solution()
print(s.numPairsDivisibleBy60([30,20,150,100,40])) # 3
print(s.numPairsDivisibleBy60([60,60,60])) # 3
print(s.numPairsDivisibleBy60([15,63,451,213,37,209,343,319]))