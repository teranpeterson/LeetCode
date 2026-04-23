# SOLVED!

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        for i in range(n):
            for j in range(m):
                if int(matrix[i][j]) == 0:
                    continue
                if int(matrix[i][j]) == 1:
                    res = max(res, 1)
                if i == 0:
                    continue
                if j == 0:
                    continue
                left, up, diag = int(matrix[i][j-1]), int(matrix[i-1][j]), int(matrix[i-1][j-1])
                matrix[i][j] = min(left, up, diag) + 1
                res = max(res, matrix[i][j])
        pprint(matrix)
        return res**2

def pprint(matrix: List[List[str]]):
    for row in matrix:
        for col in row:
            print(col, end=' ')
        print()
    print()

s = Solution()
print(s.maximalSquare(
[["1","0","1","0","0"]
,["1","0","1","1","1"]
,["1","1","1","2","2"]
,["1","0","1","2","1"]])) # 4

print(s.maximalSquare(
[["0","1"]
,["1","0"]])) # 1

print(s.maximalSquare(
[["0"]])) # 0