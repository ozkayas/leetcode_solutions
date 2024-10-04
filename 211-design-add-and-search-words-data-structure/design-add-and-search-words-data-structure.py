class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curNode = self.root
        for i, ch in enumerate(word):
            # if not exists add it in children
            if ch not in curNode.children:
                curNode.children[ch] = Node()
            curNode = curNode.children[ch]
            if i == len(word)-1:
                curNode.isWord = True

    def search(self, word: str) -> bool:
        def explore(word: str, node: Node) -> bool:
            curNode = node
            for i, w in enumerate(word):
                if w == ".":
                    # recursively search all paths possible down
                    for child in curNode.children.keys():
                        if explore(word[i + 1:], curNode.children[child]):
                            return True
                    return False
                elif w not in curNode.children:
                    return False
                else:
                    curNode = curNode.children[w]
            return curNode.isWord

        return explore(word, self.root)

        
class Node:
    def __init__(self):
        self.children = dict()
        self.isWord = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)