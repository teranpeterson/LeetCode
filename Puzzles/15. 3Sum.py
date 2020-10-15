from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        ret = set()
        for i in range(len(nums)):
            m = []
            target = -nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                x = target - nums[j]
                if x in m:
                    lst = sorted([nums[i], nums[j], x])
                    ret.add(tuple(lst))
                m.append(nums[j])

        return [list(s) for s in ret]

lst = [
    [-1,0,1,2,-1,-4], # [[-1,-1,2],[-1,0,1]]
    [], # []
    [0], # []
]
for l in lst:
    print(Solution().threeSum(l))


# 0 = 1 + 2 + -3
# -1 = 2 + -3
# -3 = -3