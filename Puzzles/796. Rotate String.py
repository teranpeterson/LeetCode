# SOLVED

class Solution():
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A

s = Solution()
print(s.rotateString("abcde", "abced"))