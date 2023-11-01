# SOLVED

from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(idx: int, subset: List[int]):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[idx])
            dfs(idx + 1, subset)
            subset.pop()
            dfs(idx + 1, subset)
        
        dfs(0, [])
        return res

s = Solution()
print(s.subsets([1,2,3]))
print(s.subsets([0]))