from collections import deque

class Solution:
    def removeOuterParentheses(self, S):
        if S == "":
            return S
        ret = ""
        stack = []
        for s in S:
            if not stack:
                stack.append(s)
                continue
            l = stack[-1]
            if s == l:
                stack.append(s)
            else:
                stack.pop()
            if stack:
                ret += s
        return ret
                

pas = [
    "(())",                 # ()
    "(()())(())",           # ()()()
    "(()())(())(()(()))",   # ()()()()(())
    "()()",                 # 
]

s = Solution()
for p in pas:
    print("Solution: " + s.removeOuterParentheses(p))