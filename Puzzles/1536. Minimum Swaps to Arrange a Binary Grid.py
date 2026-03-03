# SOLVED

# Given an n x n binary grid, in one step you can choose two adjacent rows of the grid and swap them.
# A grid is said to be valid if all the cells above the main diagonal are zeros.
# Return the minimum number of steps needed to make the grid valid, or -1 if the grid cannot be valid.
# The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends at cell (n, n).

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        loc = []
        for i in range(0, n):
            zeros = 0
            for j in range(n-1, 0, -1):
                if grid[i][j] == 0:
                    zeros += 1
                else:
                    break
            loc.append(zeros)
        
        count = 0
        for p in range(0, n):
            target = n-p-1
            if loc[p] >= target:
                continue
            else:
                idx = -1
                for q in range(p+1, n):
                    if loc[q] >= target:
                        idx = q
                        break
                if idx == -1:
                    return -1

                count += idx-p
                loc = loc[:p] + [loc[idx]] + loc[p:idx] + loc[idx+1:]

        return count



s = Solution()
print(s.minSwaps([[0,0,1],[1,1,0],[1,0,0]]) == 3)
print(s.minSwaps([[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]) == -1)
print(s.minSwaps([[1,0,0],[1,1,0],[1,1,1]]) == 0)
print(s.minSwaps([[1,0,0,0,0,0],[0,1,0,1,0,0],[1,0,0,0,0,0],[1,1,1,0,0,0],[1,1,0,1,0,0],[1,0,0,0,0,0]]) == 2)
print(s.minSwaps([[1,0,0,0,0,0],[0,0,0,1,0,0],[0,0,0,1,0,0],[0,1,0,0,0,0],[0,0,1,0,0,0],[0,0,0,0,0,1]]) == 4)
print(s.minSwaps([[0,0,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[1,1,1,1,1,0,0,0,0],[0,1,0,0,0,0,0,0,0],[1,1,1,0,1,0,0,0,0],[1,0,1,0,1,0,0,0,0],[0,1,1,1,0,0,0,0,0],[1,1,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0]]) == -1)
print(s.minSwaps([[0,1,1,0,0,0,0,0,0,0,0,0],[0,1,0,1,1,0,0,0,0,0,0,0],[0,1,1,1,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,0,0,0,0,0,0],[1,1,1,1,0,1,1,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0,0],[1,0,1,1,1,1,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,1,1,1,0,0,0,0,0],[0,0,1,1,1,0,1,0,0,0,0,0],[1,0,0,0,0,1,1,0,0,0,0,0],[0,1,0,0,0,0,0,0,0,0,0,0]]) == 12)
