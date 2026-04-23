# Solution involves time. Always draw time on a graph.

# Intuition. Calculate how many ticks it takes for each car to reach target.
# Check if any car starting ahead is slower. If so, ignore as a fleet with that car.

from typing import List
from collections import defaultdict

def fleet(target: int, position: List[int], speed: List[int]) -> int:
    stack = []
    for i in range(len(position)):
        p, s = position[i], speed[i]
        stack.append((p,s,0))

    done = defaultdict(lambda: 0)
    done2 = []
    while stack:
        p, s, t = stack.pop(0)
        if p == target:
            done[t] += 1
            done2.append((p,s,t))
            continue
        p += s
        t += 1
        stack.append((p,s,t))
    print(done2)
    return len(done)



print(fleet(12, [10,8,0,5,3], [2,4,1,1,3])) # 3

# 1 -> 1
# 2 -> 1
# 3 -> 12
# 4 -> 7
# 5 -> 3