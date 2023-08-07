from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            n = numbers[l] + numbers[r]

            if n > target:
                r -= 1
            elif n < target:
                l -= 1
            else:
                return [l + 1, r + 1]
        return []

s = Solution()
print(s.twoSum([2,7,11,15], 9) == [1,2])
print(s.twoSum([2,3,4], 6) == [1,3])
print(s.twoSum([-1,0], -1) == [1,2])