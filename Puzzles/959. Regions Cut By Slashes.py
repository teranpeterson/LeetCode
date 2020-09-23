# WORKING

class Solution:
    def regionsBySlashes(self, g):
        divs = 0
        self.grid = g
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                c = self.grid[i][j]

    def countDivs(self, i, j):
        c = self.grid[i][j]

ary = [" /",
       "/ "]

s = Solution()
print(s.regionsBySlashes(ary))