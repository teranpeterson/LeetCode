# SOLVED

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])

    stack = [intervals[0]]
    for interval in intervals[1:]:
        if stack[-1][1] >= interval[0]:
            stack[-1][1] = max(stack[-1][1], interval[1])
        else:
            stack.append(interval)
    return stack

print(merge([[1,3],[8,10],[15,18],[2,6]])) # [[1,6],[8,10],[15,18]]
