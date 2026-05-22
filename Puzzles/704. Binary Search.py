# SOLVED

from typing import List

def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    while l <= r:
        x = l+(r-l)//2
        if nums[x] == target:
            return x
        if nums[x] > target:
            r = x-1
        if nums[x] < target:
            l = x+1
    return -1

print(search([-1,0,2,4,6,8], 4)) # 3
print(search([-1,0,2,4,6,8], 3)) # -1
print(search([2,5], 5)) # 1
