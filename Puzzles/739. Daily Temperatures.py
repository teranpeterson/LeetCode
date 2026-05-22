# SOLVED

# Make sure to use pop(0) right lol

from typing import List

def daily(temperatures: List[int]) -> List[int]:
    res = [0] * len(temperatures)
    stack = []
    for idx, temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            prev_temp, prev_idx = stack.pop()
            res[prev_idx] = idx - prev_idx
        stack.append((temp, idx))

    return res

print(daily([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(daily([30,40,50,60])) # [1,1,1,0]
print(daily([30,60,90])) # [1,1,0]
