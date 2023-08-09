# SOLVED

from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = defaultdict(lambda: 0)
        for n in nums:
            if hashMap[n] > 0:
                return True
            else:
                hashMap[n] += 1
        return False

s = Solution()
print(s.containsDuplicate([1,2,3,1]) == True)
print(s.containsDuplicate([1,2,3,4]) == False)
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True)
