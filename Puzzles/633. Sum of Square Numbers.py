# SOLVED

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = math.floor(math.sqrt(c))
        for i in range(n, -1, -1):
            x = i*i
            m = c - x
            if math.sqrt(m).is_integer():
                return True
        return False

print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(3))
print(Solution().judgeSquareSum(41))