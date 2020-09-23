# SOLVED

class Solution:
    def maxAreaOfIsland(self, g):
        max = 0
        self.grid = g
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                n = self.grid[i][j]
                if n == 1:
                    self.counter = 0
                    self.checkNeighbors(i, j)
                    if self.counter > max:
                        max = self.counter
        return max

    
    def checkNeighbors(self, i, j):
        if i < 0 or i > len(self.grid) - 1:
            return
        if j < 0 or j > len(self.grid[i]) - 1:
            return
        n = self.grid[i][j]
        if n == 1:
            self.grid[i][j] = 2
            self.counter += 1
            self.checkNeighbors(i-1, j)
            self.checkNeighbors(i+1, j)
            self.checkNeighbors(i, j-1)
            self.checkNeighbors(i, j+1)


    


ary =  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,0,0,0,0],
        [0,0,0,0,0,0,0,1,0,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]



s = Solution()
print(s.maxAreaOfIsland(ary))