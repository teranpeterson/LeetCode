# SOLVED

from typing import List
from collections import defaultdict

class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        heights = defaultdict(list)

        for l, h in rectangles:
            heights[h].append(l)
        
        for _, v in heights.items():
            v.sort()
                
        res = [0] * len(points)
        for i, point in enumerate(points):
            x, y = point[0], point[1]
            count = 0
            for h in range(y, 100+1):
                lengths = heights[h]
                for n, l in enumerate(lengths):
                    if l >= x:
                        count += len(lengths) - n
                        break
            res[i] = count

        return res


s = Solution()
print(s.countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]]))
print(s.countRectangles([[1,1],[2,2],[3,3]], [[1,3],[1,1]]))