# SOLVED

# Map impl is basically the same as set but takes more space

from typing import List
from collections import defaultdict

def longest_set(nums: List[int]) -> int:
    s = set(nums)

    res = 0
    for num in nums:
        if num-1 not in s:
            count = 1
            k = 1
            while num+k in s:
                k += 1
                count += 1
            res = max(res, count)

    return res

def longest_map(nums: List[int]) -> int:
    hashmap = defaultdict(lambda: 0)

    res = 0
    for num in nums:
        hashmap[num] = 1 + hashmap[num-1] + hashmap[num+1]
        res = max(res, hashmap[num])
    return res
    
def longest_sort(nums: List[int]) -> int:
    res = 1

    curr = 1
    prev = None
    for num in sorted(nums):
        if num - 1 == prev:
            curr += 1
        else:
            res = max(res, curr)
            curr = 1
        prev = num
    return res

print(longest_set([100,4,200,1,3,2]))
