# SOLVED

# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

from typing import List

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])

        count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] >= 1:
                    single = True
                    for p in range(i+1, n):
                        if mat[p][j] >= 1:
                            single = False
                            mat[p][j] = 2
                    for q in range(j+1, m):
                        if mat[i][q] >= 1:
                            single = False
                            mat[i][q] = 2

                    if single and mat[i][j] == 1:
                        count += 1
        return count

s = Solution()
print(s.numSpecial([[1,0,0],[0,0,1],[1,0,0]]) == 1)
print(s.numSpecial([[1,0,0],[0,1,0],[0,0,1]]) == 3)
print(s.numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]) == 1)
print(s.numSpecial([[0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,1]]) == 2)
