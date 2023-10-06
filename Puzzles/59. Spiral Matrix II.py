# SOLVED

from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = []
        for _ in range(n):
            res.append([0] * n)
        
        i, j = 0, 0

        row_s, col_s = 0, 0
        row_e, col_e = n, n

        res[0][0] = 1
        m = 2

        while row_s < row_e and col_s < col_e:
            while j < col_e - 1:
                j += 1
                res[i][j] = m
                m += 1
            row_s += 1
            
            while i < row_e - 1:
                i += 1
                res[i][j] = m
                m += 1
            col_e -= 1

            if j <= col_s:
                break
            
            while j > col_s:
                j -= 1
                res[i][j] = m
                m += 1
            row_e -= 1
            
            while i > row_s:
                i -= 1
                res[i][j] = m
                m += 1
            col_s += 1
        
        return res

s = Solution()
print(s.generateMatrix(3))
print(s.generateMatrix(1))