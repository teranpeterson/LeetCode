# SOLVED

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.isTerminal = False

    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            idx = ord(c) - 97
            if curr.children[idx] == None:
                curr.children[idx] = Trie()
            curr = curr.children[idx]
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            idx = ord(c) - 97
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return curr.isTerminal

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            idx = ord(c) - 97
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('word')
param_2 = obj.search('word')
param_3 = obj.startsWith('prefix')