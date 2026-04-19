# SOLVED

# Slightly faster to just count rather than doing a full sort

from typing import List
from collections import defaultdict

def group2(strs: List[str]) -> List[List]:
    hashmap = defaultdict(list)

    for s in strs:
        key = [0]*26
        for c in s:
            key[ord(c) - ord("a")] += 1
        hashmap[tuple(key)].append(s)
    return list(hashmap.values())

def group(strs: List[str]) -> List[List]:
    hashmap = defaultdict(list)
    
    for s in strs:
        hashmap[str(sorted(s))].append(s)
    
    return list(hashmap.values())

print(group2(["eat", "tea", "tan", "ate", "nat", "bat"]))
