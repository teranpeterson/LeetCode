# SOLVED

def valid(s: str) -> bool:
    stack = []

    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
        else:
            x = stack.pop(0)
            if x == "(" and c == ")":
                continue
            elif x == "[" and c == "]":
                continue
            elif x == "{" and c == "}":
                continue
            else:
                return False
    return len(stack) == 0

print(valid("()"))
print(valid("()[]{}"))
