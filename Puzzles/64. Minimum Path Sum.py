# SOLVED

class Solution:
    def minPathSum(self, grid):
        if not grid:
            return grid
        h = len(grid)
        l = len(grid[0])
        m = []
        for i in range(h):
            m.append([])
            for j in range(l):
                m[i].append(0)
        m[0][0] = grid[0][0]
        for i in range(h):
            for j in range(l):
                if i == 0 and j == 0:
                    continue
                a = m[i-1][j]
                b = m[i][j-1]
                if i-1 < 0:
                    a = float('inf')
                if j-1 < 0:
                    b = float('inf')
                m[i][j] = grid[i][j] + min(a, b)
        return m[-1][-1]



pas = [
    [
        [1,3,1],
        [1,5,1],
        [4,2,1],
    ],  # 7
]

s = Solution()
for p in pas:
    print(s.minPathSum(p))