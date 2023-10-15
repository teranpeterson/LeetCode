# SOLVED

from typing import List

class Solution:
    # Use constraints to prevent generating bad cases (num each time of paren < n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(s):
            if len(s) == n * 2:
                if self.checker(s):
                    res.append(s)
            else:
                helper(s + "(")
                helper(s + ")")
        
        helper("")
        return list(res)
    
    def checker(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if not stack:
                    return False
                stack.pop()
        if not stack:
            return True
        return False

s = Solution()
print(s.checker("()()"))
print(s.checker("())"))
print(s.checker("(()"))
print(s.checker(""))
print(s.checker("(())"))
print(s.generateParenthesis(3))
print(s.generateParenthesis(1))