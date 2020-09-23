# SOLVED

class Solution:
    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0
        ret = 0
        start = 0
        end = len(height)-1
        while start != end:
            vol = (end - start) * min(height[end], height[start])
            if vol > ret:
                ret = vol
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return ret

pas = [
    [1,8,6,2,5,4,8,3,7],        # 49
]

s = Solution()
for p in pas:
    print("Solution: " + str(s.maxArea(p)))