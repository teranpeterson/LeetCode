# SOLVED

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '[' or c == '{' or c == '(':
                stack.append(c)
            else:
                if not stack:
                    return False
                t = stack.pop()
                if t == '[' and c != ']':
                    return False
                if t == '{' and c != '}':
                    return False
                if t == '(' and c != ')':
                    return False
        if stack:
            return False
        return True

s = Solution()
print(s.isValid("()") == True)
print(s.isValid("()[]{}") == True)
print(s.isValid("(]") == False)
print(s.isValid("[") == False)
print(s.isValid("]") == False)