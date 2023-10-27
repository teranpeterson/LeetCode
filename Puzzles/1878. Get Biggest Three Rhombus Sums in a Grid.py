# WORKING

from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        max_r_size = min(len(grid), len(grid[0]))
        if max_r_size % 2 == 0:
            max_r_size -= 1

        k1 = 0
        k2 = 0
        k3 = 0

        for r_size in range(1, max_r_size + 1, 2):
            half = r_size // 2
            for i in range(0, len(grid)):
                if i + r_size > len(grid):
                    continue
                for j in range(0, len(grid[0])):
                    if j + half >= len(grid[0]):
                        continue
                    if j - half < 0:
                        continue
                    sum = 0
                    for n in range(0, r_size):
                        j_mod = 0
                        if n == half:
                            j_mod = half
                        elif half > 0:
                            j_mod = n % half
                        sum += grid[i+n][j+j_mod]
                        if j_mod != 0:
                            sum += grid[i+n][j-j_mod]
                    
                    if sum == k1 or sum == k2 or sum == k3:
                        continue
                    if sum > k3:
                        k1 = k2
                        k2 = k3
                        k3 = sum
                    elif sum > k2:
                        k1 = k2
                        k2 = sum
                    elif sum > k1:
                        k1 = sum
        
        res = []
        if k3 > 0:
            res.append(k3)
        if k2 > 0:
            res.append(k2)
        if k1 > 0:
            res.append(k1)
        return res

s = Solution()
print(s.getBiggestThree([[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]))
print(s.getBiggestThree([[1,2,3],[4,5,6],[7,8,9]]))
print(s.getBiggestThree([[7,7,7]]))