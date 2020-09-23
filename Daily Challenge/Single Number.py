class Solution:
    def singleNumber(self, nums):
        m = []
        for n in nums:
            if n in m:
                m.remove(n)
            else:
                m.append(n)
        return m[0]
        



pas = [
    [2,2,1],
    [4,1,2,1,2],
]

s = Solution()
for p in pas:
    print(s.singleNumber(p))
