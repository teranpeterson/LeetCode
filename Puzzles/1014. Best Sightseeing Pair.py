# SOLVED

class Solution:
    def maxScoreSightseeingPair(self, A):
        ret = 0
        if not A:
            return ret
        idx = 0
        for i in range(1, len(A)):
            x = A[idx] + A[i] + idx - i
            if x > ret:
                ret = x
            dif = i - idx
            if A[i] > A[idx]-dif:
                idx = i
        return ret


pas = [
    [8,1,5,2,6],            # 11
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.maxScoreSightseeingPair(p)))














# m = 0
# if not A:
#     return m
# for i in range(len(A)):
#     for j in range(len(A)):
#         if i == j:
#             continue
#         if i >= j:
#             continue
#         print(str(i) + "=" + str(A[i]))
#         print(str(j) + "=" + str(A[j]))
#         print("x = " + str(A[i]) + " + " + str(A[j]) + " + " + str(i) + " - " + str(j))
#         x = A[i] + A[j] + i - j
#         print("x=" + str(x))
#         print()
#         if x > m:
#             m = x
# return m