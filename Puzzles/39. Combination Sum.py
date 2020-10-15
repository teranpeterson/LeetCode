# SOLVED

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        m = {}
        out = []
        for n in candidates:
            if target < 1:
                return out
            if n == target and [n] not in out:
                out.append([n])
            x = target - n
            if x in candidates:
                sub = [n, x]
                sub.sort()
                out.append([n, x])
            subs = self.combinationSum(candidates, x)
            for sub in subs:
                if sub:
                    sub.append(n)
                    sub.sort()
                    out.append(sub)
        ret = []
        for o in out:
            o.sort()
            if o not in ret:
                ret.append(o)
        return sorted(ret)

print(sorted(Solution().combinationSum([2,7,6,3,5,1], 9)))
print(sorted([[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,2],[1,1,1,1,1,1,3],[1,1,1,1,1,2,2],[1,1,1,1,2,3],[1,1,1,1,5],[1,1,1,2,2,2],[1,1,1,3,3],[1,1,1,6],[1,1,2,2,3],[1,1,2,5],[1,1,7],[1,2,2,2,2],[1,2,3,3],[1,2,6],[1,3,5],[2,2,2,3],[2,2,5],[2,7],[3,3,3],[3,6]]))