# SOLVED

# Min heap adds minor improvement. But using bounded buckets gives linear solution

from typing import List
from collections import defaultdict
from heapq import heapify, heappop

def topK_optimal(nums: List[int], k: int) -> List[int]:
    counter = defaultdict(lambda: 0)
    
    for num in nums:
        counter[num] += 1
    
    bucket = [[] for _ in range(len(nums) + 1)]
    for num, count in counter.items():
        bucket[count].append(num)
    
    res = []
    for idx in range(len(nums), -1, -1):
            for num in bucket[idx]:
                res.append(num)
                if len(res) == k:
                    return res
    
    return res



def topK_heap(nums: List[int], k: int) -> List[int]:
    counter = defaultdict(lambda: 0)
    
    for num in nums:
        counter[num] += 1

    heap = [(-count, num) for num, count in counter.items()]
    heapify(heap)

    res = []
    for _ in range(k):
        res.append(heappop(heap)[1])
    return res

def topK_sort(nums: List[int], k: int) -> List[int]:
    counter = defaultdict(lambda: 0)
    
    for num in nums:
        counter[num] += 1

    return [num for num, _ in sorted(counter.items(), key=lambda item: item[1], reverse=True)][:k]

print(topK_optimal([0,8,4,4,5,7,7,7,3,1,2,4,7,7], 2))
print(topK_optimal([1], 1))
