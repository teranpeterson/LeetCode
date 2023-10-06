# SOLVED

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = [matrix[0][0]]

        m = len(matrix[0]) - 1
        n = len(matrix) - 1

        col_s = 0
        col_e = len(matrix[0]) - 1

        row_s = 0
        row_e = len(matrix) - 1

        i = 0
        j = 0

        while True:
            while j < col_e:
                j += 1
                l.append(matrix[i][j])
            row_s += 1

            if i >= row_e:
                break

            while i < row_e:
                i += 1
                l.append(matrix[i][j])
            col_e -= 1

            if j <= col_s:
                break

            while j > col_s:
                j -= 1
                l.append(matrix[i][j])
            row_e -= 1

            if i <= row_s:
                break

            while i > row_s:
                i -= 1
                l.append(matrix[i][j])
            col_s += 1

            if j >= col_e:
                break
        
        return l
            

            


s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))