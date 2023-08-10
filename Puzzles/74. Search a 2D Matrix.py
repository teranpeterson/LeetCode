# SOLVED

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i, j = 0, n * m - 1

        while i <= j:
            k = i + (j - i) // 2
            n = matrix[k // m][k % m]

            if n > target:
                j = k - 1
            elif n < target:
                i = k + 1
            else:
                return True
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))

# 3 x 4
# [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#   0 1 2 3    4  5  6  7    8  9 10 11
# 0 0 1 2 3  1 0  1  2  3  2 0  1  2  3

