# SOLVED

class Solution:
    def isHappy(self, n):
        sum = n
        sums = []
        while sum != 1:
            m = sum
            sum = 0
            for x in str(m):
                sum += int(x)**2
            if sum in sums:
                return False
            sums.append(sum)
        return True