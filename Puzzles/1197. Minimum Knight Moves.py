class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(2, 1), (1, 2), (-2, -1), (-1, -2), (2, -1), (1, -2), (-2, 1), (-1, 2)]

        queue = [(0,0,0)]
        visited = set()
        visited.add((0,0))
        while queue:
            loc_x,loc_y,s = queue.pop(0)
            if loc_x == x and loc_y == y:
                return s

            for new_x, new_y in directions:
                new_x += loc_x
                new_y += loc_y
                if (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, s + 1))
                    visited.add((new_x, new_y))
        

print(Solution().minKnightMoves(100, 100))