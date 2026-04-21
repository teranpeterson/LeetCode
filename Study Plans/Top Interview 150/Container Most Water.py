# SOLVED

from typing import List

def mostWater(height: List[int]) -> int:
    l, r = 0, len(height) - 1

    res = 0
    while l < r:
        curr = min(height[l], height[r]) * (r-l)
        res = max(res, curr)
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        else:
            l += 1
    return res
        

print(mostWater([1,8,6,2,5,4,8,3,7])) # 49
