# SOLVED

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float("inf")
        high = float("-inf")
        max = 0
        for n in prices:
            if n < low:
                low = n
                high = float("-inf")
            if n > high:
                high = n
            new_max = high-low
            if new_max > max:
                max = new_max
        return max

