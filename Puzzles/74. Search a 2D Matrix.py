

from typing import List

def search(matrix: List[List[int]], target: int) -> bool:




    l, r = 0, len(matrix)*len(matrix[0])-1
    for n in range(r):
        print(matrix[n//len(matrix[0])][n%len(matrix[0])])
    while l <= r:
        x = l+(r-l)//2
        r, c = x // len(matrix), x % len(matrix)
        if matrix[r][c] == target:
            return True
        if matrix[r][c] > target:
            r = x-1
        if matrix[r][c] < target:
            l = x+1
    return False

print(search([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10)) # true
print(search([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 15)) # false