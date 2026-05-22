# SOLVED

# More efficient to use a set

from typing import List

class Trie:
    def __init__(self):
        self.children = {}
        self.terminal = False


def word(s: str, wordList: List[str]) -> bool:
    t = Trie()

    for word in wordList:
        curr = t
        for c in word:
            if c not in curr.children:
                x = Trie()
                curr.children[c] = x
            curr = curr.children[c]
        curr.terminal = True
    
    memo = {}
    def test(start: int) -> bool:
        if start in memo:
            return memo[start]
        state = t
        for i in range(start, len(s)):
            c = s[i]
            if state.terminal:
                if test(i):
                    memo[start] = True
                    return True
            if c not in state.children:
                memo[start] = False
                return False
            state = state.children[c]
        memo[start] = state.terminal
        return state.terminal
    
    return test(0)


print(word("leetcode", ["leet", "code"])) # True
print(word("leetcode", ["lee", "leet", "code"])) # True
print(word("applepenapple", ["apple", "pen"])) # True
print(word("catsandog", ["cats", "dog", "sand", "and", "cat"])) # False
