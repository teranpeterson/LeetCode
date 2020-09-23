# SOLVED

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        if len(intervals) <= 1:
            return intervals
        if not intervals[0]:
            return [[]]
        
        intervals = sorted(intervals, key=lambda x: (x[0],x[1]))

        i = 1
        prev = intervals[0][0]
        find = intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] >= prev and intervals[i][0] <= find:
                new_int = []
                if intervals[i][1] > find:
                    new_int = [prev, intervals[i][1]]
                else:
                    new_int = [prev, find]
                del intervals[i]
                intervals[i-1] = new_int
                prev = new_int[0]
                find = new_int[1]
            else:
                prev = intervals[i][0]
                find = intervals[i][1]
                i += 1
        return intervals

pas = [
    [[1,3],[2,6],[8,10],[15,18]],       # [[1,6],[8,10],[15,18]]
    [[1,4],[4,5]],                      # [[1,5]]
    [[1,5],[1,5]],                      # [[1,5]]
    [[1,3],[2,3]],                      # [[1,3]]
    [[1,3],[2,4],[3,5]],                # [[1,5]]
    [[1,5]],                            # [[1,5]]
    [],                                 # []
    [[]],                               # [[]]
    [[1,4],[0,4]],                      # [[0,4]]
    [[1,4],[0,1]],                      # [[0,4]]
    [[1,4],[2,4]],                      # [[1,4]]
    [[3,5],[1,4]],                      # [[1,5]]
    [[3,5],[1,7]],                      # [[1,7]]
    [[1,4],[0,2],[3,5]],                # [[0,5]]
    [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]],    # [[1,3],[4,7]]
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.merge(p)))