# SOLVED

from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for circle in circles:
            x, y, r = circle[0], circle[1], circle[2]
            for i in range(x-r,x+r+1):
                for j in range(y-r,y+r+1):
                    if (i - x)**2 + (j - y)**2 <= r**2:
                        res.add((i,j))
        print(res)
        return len(res)

s = Solution()
print(s.countLatticePoints([[2,2,1]]))
print(s.countLatticePoints([[2,2,2],[3,4,1]]))