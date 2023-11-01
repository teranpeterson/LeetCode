# SOLVED

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx: int, sum: int, subset: List[int]):
            if sum == target:
                res.append(subset.copy())
                return
            
            if idx >= len(candidates):
                return
            
            if sum + candidates[idx] <= target:
                subset.append(candidates[idx])
                dfs(idx, sum + candidates[idx], subset)
                subset.pop()
            dfs(idx + 1, sum, subset)
        
        dfs(0, 0, [])

        return res

s = Solution()
print(s.combinationSum([2,3,6,7], 7))
print(s.combinationSum([2,3,5], 8))
print(s.combinationSum([2], 1))