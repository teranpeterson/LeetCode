from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(lambda: [])
        for str in strs:
            hashMap[tuple(sorted(str))].append(str)
        res = []
        for _, value in hashMap.items():
            res.append(value)
        return res


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(s.groupAnagrams([""]))
print(s.groupAnagrams(["a"]))