from collections import defaultdict
from typing import List

class Solution:
    def getSqr(self, row: int, col: int) -> int:
        if row < 3:
            if col < 3:
                return 0
            elif col < 6:
                return 1
            else:
                return 2
        elif row < 6:
            if col < 3:
                return 3
            elif col < 6:
                return 4
            else:
                return 5
        else:
            if col < 3:
                return 6
            elif col < 6:
                return 7
            else:
                return 8

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(lambda: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        cols = defaultdict(lambda: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        sqrs = defaultdict(lambda: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

        for i, row in enumerate(board):
            for j, number in enumerate(row):
                if number == ".":
                    continue
                n = int(number)

                if rows[i][n] == 0:
                    return False
                else:
                    rows[i][n] -= 1
                
                if cols[j][n] == 0:
                    return False
                else:
                    cols[j][n] -= 1
                
                s = self.getSqr(i, j)
                if sqrs[s][n] == 0:
                    return False
                else:
                    sqrs[s][n] -= 1
        
        return True
        


pas = [
    [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ],  # true
    [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ],  # false
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.isValidSudoku(p)))