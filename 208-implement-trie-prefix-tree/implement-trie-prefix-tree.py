class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.isWord = False

    def insert(self, word: str) -> None:
        curNode = self.root

        for i in range(len(word)):
            cur = word[i]
            idx_cur = ord(cur) - ord('a')

            # If no index to insert this character
            if curNode.children[idx_cur] == None:
                curNode.children[idx_cur] = TrieNode()
            
            # Switch to next node
            curNode = curNode.children[idx_cur]

            if i == len(word)-1:
                curNode.isWord = True
                return


        

    def search(self, word: str) -> bool:
        curNode = self.root
        
        for w in word:
            idx = ord(w)-ord("a")
            node_for_w = curNode.children[idx]


            if node_for_w == None: # This letter not exists so return False
                return False

            curNode = node_for_w
        
        return curNode.isWord
            





        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        
        for w in prefix:
            idx = ord(w)-ord("a")
            node_for_w = curNode.children[idx]


            if node_for_w == None: # This letter not exists so return False
                return False

            curNode = node_for_w
        
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None for _ in range(26)]