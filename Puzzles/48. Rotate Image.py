# SOLVED

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        m = 0
        while m < n:
            for j in range(m, n):
                replaced = matrix[m][j]
                replaced, matrix[j][n] = matrix[j][n], replaced
                replaced, matrix[n][n-j+m] = matrix[n][n-j+m], replaced
                replaced, matrix[n-j+m][m] = matrix[n-j+m][m], replaced
                replaced, matrix[m][j] = matrix[m][j], replaced
            n -= 1
            m += 1
            print(matrix)



s = Solution()
s.rotate([[4,8],[3,6]])
s.rotate([[1,2,3],[4,5,6],[7,8,9]])
s.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])