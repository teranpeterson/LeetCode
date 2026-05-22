# SOLVED

from typing import List

def maxAreaOfIsland(grid: List[List[int]]) -> int:
    def dfs(i: int, j: int) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0
        val = grid[i][j]
        if val != 1:
            return 0
        grid[i][j] = 2
        return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
    
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            val = grid[i][j]
            if val != 1:
                continue
            res = max(res, dfs(i, j))
    return res
          

print(maxAreaOfIsland([
[0,1,1,0,1],
[1,0,1,0,1],
[0,1,1,0,1],
[0,1,0,0,1]])) # 6
