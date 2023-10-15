# SOLVED

from typing import List

class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        word_chunks = [word]

        m = set()
        smallest = float('inf')
        largest = 0
        for f in forbidden:
            m.add(f)
            smallest = min(smallest, len(f))
            largest = max(largest, len(f))

        for dist in range(smallest, largest + 1):
            new_chunks = []
            while word_chunks:
                chunk = word_chunks.pop()
                if len(chunk) < dist:
                    new_chunks.append(chunk)
                    continue

                l, r = 0, dist
                start = 0
                while r < len(chunk) + 1:
                    if chunk[l:r] in m:
                        new_chunks.append(chunk[start:r-1])
                        l += 1
                        r += 1
                        start = l
                    else:
                        l += 1
                        r += 1
                    
                new_chunks.append(chunk[start:])
            word_chunks = new_chunks
        
        res = 0
        for chunk in word_chunks:
            res = max(res, len(chunk))
        
        return res


s = Solution()
print(s.longestValidSubstring("cbaaaabc", ["aaa","cb"])) # 4
print(s.longestValidSubstring("leetcode", ["de","le","e"])) # 4
print(s.longestValidSubstring("acbc", ["cbc","acb","acb","acbc"])) # 2
print(s.longestValidSubstring("bcac", ["bcac","caca","bcac","bca"])) # 3