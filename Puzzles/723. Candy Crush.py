# SOLVED

from typing import List

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])

        while True:
            dirty = [0] * m
            for i in range(n):
                for j in range(m):
                    if board[i][j] == 0:
                        continue
                    
                    if j < m - 2 and abs(board[i][j]) == abs(board[i][j+1]) == abs(board[i][j+2]):
                        if board[i][j] > 0:
                            board[i][j]  =  -board[i][j]
                        if board[i][j+1] > 0:
                            board[i][j+1] = -board[i][j+1]
                        if board[i][j+2] > 0:
                            board[i][j+2] = -board[i][j+2]
                        dirty[j] = 1
                        dirty[j+1] = 1
                        dirty[j+2] = 1
                    
                    if i < n - 2 and abs(board[i][j]) == abs(board[i+1][j]) == abs(board[i+2][j]):
                        if board[i][j] > 0:
                            board[i][j]   = -board[i][j]
                        if board[i+1][j] > 0:
                            board[i+1][j] = -board[i+1][j]
                        if board[i+2][j] > 0:
                            board[i+2][j] = -board[i+2][j]
                        dirty[j] = 1

            stable = True
            for j, v in enumerate(dirty):
                if v == 1:
                    stable = False
                    i = n-1
                    offset = 1
                    while i > -1:
                        if board[i][j] <= 0:
                            if i - offset >= 0:
                                board[i][j] = board[i-offset][j]
                                board[i-offset][j] = 0
                                i += 1
                            else:
                                board[i][j] = 0
                            offset += 1
                        else:
                            if offset > 1:
                                offset -= 1
                        i -= 1
            
            if stable:
                break

        return board
                

s = Solution()
print(s.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]) == [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]])
print(s.candyCrush([[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]) == [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]])
print(s.candyCrush([[5,4,5,3,1],[1,3,2,2,3],[4,2,4,1,2],[2,5,1,1,1],[2,2,3,5,4]]) == [[5,0,0,0,0],[1,4,0,0,1],[4,3,5,3,3],[2,5,4,1,2],[2,2,3,5,4]])
print(s.candyCrush([[5,5,5,3,2],[3,4,3,2,4],[3,2,3,4,2],[1,1,2,3,1],[5,3,4,4,3]]) == [[0, 0, 0, 3, 2], [3, 4, 3, 2, 4], [3, 2, 3, 4, 2], [1, 1, 2, 3, 1], [5, 3, 4, 4, 3]])