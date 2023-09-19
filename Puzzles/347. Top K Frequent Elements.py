# SOLVED

from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = Counter(nums)
        return [k for k, v in sorted(m.items(), key=lambda item: item[1], reverse=True)][:k]

s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2) == [1,2])
print(s.topKFrequent([1], 1) == [1])
print(s.topKFrequent([-1,-1], 1) == [-1])