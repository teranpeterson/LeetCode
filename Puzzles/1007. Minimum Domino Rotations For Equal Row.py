# SOLVED

class Solution:
    def minDominoRotations(self, A, B):
        count = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for i in range(len(A)):
            count[A[i]] += 1
            count[B[i]] += 1
        print(count)
        num = max(count, key=lambda k: count[k])
        print(num)
        top = 0
        bot = 0
        for i in range(len(A)):
            if A[i] == num or B[i] == num:
                if A[i] != num:
                    top += 1
                if B[i] != num:
                    bot += 1
            else:
                return -1
        return min(top, bot)



A = [2,1,2,4,2,2]
B = [5,2,6,2,3,2]
# Output: 2

# A = [3,5,1,2,3]
# B = [3,6,3,3,4]
# Output: -1

# A = [1,2,1,1,1,2,2,2]
# B = [2,1,2,2,2,2,2,2]
# Output: 1

s = Solution()
print("Solution: " + str(s.minDominoRotations(A, B)))