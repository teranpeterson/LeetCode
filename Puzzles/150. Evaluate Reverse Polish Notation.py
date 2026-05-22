# SOLVED

from typing import List

def polish(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token.isnumeric():
            stack.append(int(token))
        else:
            a = stack.pop(0)
            b = stack.pop(0)
            if token == "+":
                stack.append(a+b)
            if token == "*":
                stack.append(a*b)
    return stack.pop()
                

print(polish(["2", "1", "+", "3", "*"])) # 9
