from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: (x[1], x[2]))
        i = 1
        cur = trips[0][0]
        while trips and i < len(trips):
            j = 0
            while j < i:
                if trips[i][1] >= trips[j][2]:
                    cur -= trips[j][0]
                    trips.pop(j)
                    i -= 1
                else:
                    j += 1
            cur += trips[i][0]
            if cur > capacity:
                return False
            i += 1
        return True


# inp = [[2,1,5],[3,3,7]]
inp = [[2,1,5],[3,5,7]]
# inp = [[1,2,4],[3,2,7],[3,7,9],[7,3,9]]

print(Solution().carPooling(inp, 3))
