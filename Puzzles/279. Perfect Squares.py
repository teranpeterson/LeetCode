# WORKING

import math

class Solution:
    def numSquares(self, n):
        dp = [0] + [float('inf')]*n
        print(dp)
        for i in range(1, n+1):
            for j in range(1, int(i**0.5)+1):
                print("i=" + str(i))
                print("j=" + str(j))
                print()
            dp[i] = min(dp[i-j*j] for j in range(1, int(i**0.5)+1)) + 1
        print(dp)
        return dp[n]
        # p = 2
        # perf = [1]
        # while perf[-1] < n:
        #     perf.append(p**2)
        #     p += 1
        # del perf[-1]
        # print(perf)
        
        # i = len(perf)-1
        # j = len(perf)-1
        # ret = float('inf')
        # while i >= 0 and j >= 0:

        

pas = [
    12,     # 3
    13,     # 2
]

s = Solution()
for p in pas:
    print(s.numSquares(p))