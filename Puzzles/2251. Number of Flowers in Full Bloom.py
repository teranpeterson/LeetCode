# SOLVED

from typing import List
import heapq

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i, p in enumerate(people)]
        people.sort()

        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)

        res = [0] * len(people)

        count = 0
        for p, i in people:
            while start and start[0] <= p:
                heapq.heappop(start)
                count += 1
            while end and end[0] < p:
                heapq.heappop(end)
                count -= 1
            res[i] = count
        return res

s = Solution()
print(s.fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
print(s.fullBloomFlowers([[1,10],[3,3]], [3,3,2]))