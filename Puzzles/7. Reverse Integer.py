# SOLVED

class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2**31 - 1
        min_int = -2**31
        
        n = 0
        while (x > 0):
            print(n*10 + x%10)
            n = n*10 + x%10
            x = x/n
        
        if n > max_int or n < min_int:
            return 0
        return n

s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(1534236469))