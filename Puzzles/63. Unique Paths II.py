# SOLVED

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        val = 1
        for i in range(m):
            if (obstacleGrid[0][i] == 1):
                obstacleGrid[0][i] = "x"
                val = 0
            else:
                obstacleGrid[0][i] = val
        if (obstacleGrid[0][0] == "x"):
            return 0
        val = 1
        for i in range(1, n):
            if (obstacleGrid[i][0] == 1):
                obstacleGrid[i][0] = "x"
                val = 0
            else:
                obstacleGrid[i][0] = val
        for i in range(1, n):
            for j in range(1, m):
                if (obstacleGrid[i][j] == 1):
                    obstacleGrid[i][j] = "x"
                    continue
                a = obstacleGrid[i-1][j]
                b = obstacleGrid[i][j-1]
                if a == "x":
                    a = 0
                if b == "x":
                    b = 0
                obstacleGrid[i][j] = a + b
        x = obstacleGrid[n-1][m-1]
        if x == "x":
            return 0
        else:
            return x


pas = [
    [[1]],      # 0
    [[1],[0]],  # 0
    [[1,1]],    # 0
    [[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0]],      # 12
    [[0,1,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,1,0,0,0]],      # 0
    [[0,0,0],[0,1,0],[0,0,0]],                              # 2
]
s = Solution()
for p in pas:
    print("Solution: " + str(s.uniquePathsWithObstacles(p)))
