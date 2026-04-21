# SOLVED

# Much better to just use 2 pointers from one end and the other
# Track max height so far for each and calculate

# Also can precompute max height for each point and store

from typing import List

def trap(height: List[int]) -> int:
    if len(height) < 2:
        return 0
    l, r = 0, 1

    total = 0
    curr = 0
    while r < len(height):
        if height[r] < height[l]:
            curr = max(curr, height[r])
            r += 1
        else:
            wall = min(height[l], height[r])
            print(f'{l} -> {r}')
            while l < r:
                total += wall - height[l]
                l += 1
            print(total)
            r += 1
    
    wall = min(curr, height[l])
    while l < len(height):
        total += wall - height[l]
        l += 1
    return total

print(trap([0,1,0,2,1,0,1,3,2,1,2,1])) # 6
