# SOLVED

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                r = stack.pop()
                l = stack.pop()
                stack.append(l + r)
            elif token == "-":
                r = stack.pop()
                l = stack.pop()
                stack.append(l - r)
            elif token == "*":
                r = stack.pop()
                l = stack.pop()
                stack.append(l * r)
            elif token == "/":
                r = stack.pop()
                l = stack.pop()
                stack.append(int(l / r))
            else:
                stack.append(int(token))
        
        return stack[0]

s = Solution()
print(s.evalRPN(["2","1","+","3","*"]) == 9)
print(s.evalRPN(["4","13","5","/","+"]) == 6)
print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22)