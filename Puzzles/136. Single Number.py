# SOLVED

class Solution:
    def singleNumber(self, nums):
        m = []
        for n in nums:
            if n in m:
                m.remove(n)
            else:
                m.append(n)
        return m[0]