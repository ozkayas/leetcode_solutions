class Node:
    def __init__(self):
        self.children = dict()
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self, word:str):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
            curr.count += 1

    def count_pref(self, word:str) -> int:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return 0
            else:
                curr = curr.children[ch]
        return curr.count

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.add_word(word)

        return trie.count_pref(pref)
        