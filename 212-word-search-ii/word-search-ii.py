class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:


        def canVisit(r:int, c:int)->bool:
            return 0 <= r < R and 0 <= c < C and board[r][c] != "#"

        def explore(r,c, trieNode:TrieNode):
            ch = board[r][c]
            if ch not in trieNode.children:
                return
            # hold original value for backtracking 
            originalValue = board[r][c]
            node = trieNode.children[ch]
            if node.word:
                ans.append(node.word)
                node.word = None # Clear since this word is added

            board[r][c] = "#"
            for rr, cc in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if canVisit(rr,cc):
                    explore(rr,cc,trieNode.children[ch])
            board[r][c] = originalValue

        root = TrieNode()
        for word in words:
            root.addWord(word)

        R, C = len(board), len(board[0])
        ans = []

        for r in range(R):
            for c in range(C):
                explore(r,c,root)

        return ans