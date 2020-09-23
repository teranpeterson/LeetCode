# WORKING

import time

class Solution:
    def trap(self, height):
        if len(height) < 3:
            return 0
        self.m = {}
        self.ret = 0
        self.h = height
        for i in range(len(height)):
            n = height[i]
            if n not in self.m:
                self.m[n] = []
            self.m[n].append(i)
        self.parse()
        return self.ret
    
    def parse(self):
        print("Staring parse")
        plus = []
        k = max(self.m)
        r = min(self.m)
        while k != r:
            # print(self.m)
            row = sorted(self.m.pop(k))
            # print(row)
            for i in range(len(row)):
                if len(row) > 1 and i >= 0 and i < len(row) - 1:
                    x = row[i]
                    y = row[i+1]
                    if y - x > 1:
                        # print(str(x) + "," + str(y))
                        self.ret += self.calc_depth(k, x, y)
                        for z in range(x+1,y):
                            plus.append(z)
                        # print(plus)
            k = max(self.m)
            self.m[k] += row + plus
            # print()
        return
    
    def calc_depth(self, m, i, j):
        n = 0
        for x in range(i+1, j):
            n += (m-self.h[x])
        return n


pas = [
    [0,1,0,2,1,0,1,3,2,1,2,1],      # 6
    [3,2,1,0,1,2,3],                # 9
    [2,1,1,1,2],                    # 3
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0],  # 0
    [0,0,1,2,3,2,1,0,0],            # 0
    [],                             # 0
    [3,0,3],                        # 3
]

import ast

lst = []
with open("long.txt", "r+") as file:
    s = file.read()
    lst = ast.literal_eval(s)

s = Solution()
# for p in pas:
#     print("Solution: " + str(s.trap(p)))
start_time = time.time()
print("Solution: " + str(s.trap(lst)))
end_time = time.time()
print("Runtime: " + str(end_time - start_time))


#  0  1  2  3  4  5  6  7  8  9  10 11
# [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#           |           |  |     |
#     |     |  |     |