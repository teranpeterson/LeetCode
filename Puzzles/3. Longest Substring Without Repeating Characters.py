# SOLVED

from collections import defaultdict

def longest(s: str) -> int:
    l, r = 0, 0
    res = 0

    hashmap = defaultdict(lambda: 0)
    while r < len(s):
        hashmap[s[r]] += 1
        print(s[l:r])
        if hashmap[s[r]] == 1:
            res = max(res, r-l+1)
        while l < len(s) and hashmap[s[r]] > 1:
            hashmap[s[l]] -= 1
            l += 1
        r += 1
    return res


print(longest("abcabcbb")) # 3
print(longest("bbbbb")) # 1 
print(longest("pwwkew")) # 3