# SOLVED

class Solution:
    def uniquePaths(self, m, n):
        paths = []
        top = []
        for i in range(m):
            top.append(1)
        paths.append(top)
        for i in range(1, n):
            paths.append([1])
        for i in range(1, n):
            for j in range(1, m):
                a = paths[i-1][j]
                b = paths[i][j-1]
                paths[i].append(a+b)
        return paths[n-1][m-1]


m = 7
n = 3
s = Solution()
print("Solution: " + str(s.uniquePaths(m, n)))



# [
#     [0,1,2,3,4,5,6]
#     [1]
#     [2]
# ]