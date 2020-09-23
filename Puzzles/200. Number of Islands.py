# SOLVED

class Solution:
    def numIslands(self, grid):
        count = 0
        self.g = grid
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                n = self.g[i][j]
                if n == "1":
                    self.count_island(i, j)
                    count += 1
        return count
    
    def count_island(self, i, j):
        if i < 0:
            return
        if i > len(self.g)-1:
            return
        if j < 0:
            return
        if j > len(self.g[i])-1:
            return
        if self.g[i][j] != "1":
            return
        self.g[i][j] = "2"
        self.count_island(i, j+1)
        self.count_island(i, j-1)
        self.count_island(i+1, j)
        self.count_island(i-1, j)
    
    def print_grid(self):
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                print(self.g[i][j], end=" ")
            print()
        print()
        

island = [["1","1","1"],
          ["0","1","0"],
          ["1","1","1"]]
s = Solution()
print("Solution: " + str(s.numIslands(island)))
