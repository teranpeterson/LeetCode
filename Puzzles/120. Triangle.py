# SOLVED

class Solution:
    def minimumTotal(self, triangle):
        if not triangle:
            return triangle
        for i in range(1, len(triangle)):
            row = triangle[i]
            for j in range(len(row)):
                a = float('inf')
                try:
                    a = triangle[i-1][j]
                except:
                    a = float('inf')
                b = triangle[i-1][j-1]
                if j-1 < 0:
                    b = float('inf')
                triangle[i][j] += min(a,b)
        return min(triangle[-1])

pas = [
    [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ], #11
    [
        [-1],
        [ 2, 3],
        [ 1,-1,-3]
    ], # -1
    [
                    [-1],
                   [ 9,-2],
                  [ 0, 4, 5],
                 [ 7, 4,-4,-5],
                [ 9, 6, 0, 5, 7],
               [ 9, 2,-9,-4, 5,-2],
              [-4,-9,-5,-7,-5,-5,-2],
             [-9, 5,-6,-4, 4, 1, 6,-4],
            [-4, 3, 9,-2, 8, 6,-9,-2,-2],
           [ 7,-6, 9, 8,-4, 2,-4,-2,-1,-2],
          [ 0, 3, 2, 4, 0,-6, 7, 6, 7,-5, 2],
         [ 9, 0,-8, 6, 4, 6, 2, 5,-9, 9,-1,-6],
        [ 6,-3,-4,-5, 0, 3, 3, 4,-6,-4,-7, 7, 3],
    ], # -33
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.minimumTotal(p)))