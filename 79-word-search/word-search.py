class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        R, C = len(board), len(board[0])
        visited = set() #to hold coordinates


        def dfs(i, r, c) -> bool:
            # print("visiting", r ,c, "for ", word[i])
            if board[r][c] != word[i]:
                return False
            if i == N-1 and board[r][c] == word[i]:
                return True
            
            original = board[r][c]
            board[r][c] = "*"

            east = False if c+1 == C else dfs(i+1, r, c+1)
            west = False if c == 0 else dfs(i+1, r, c-1)
            north = False if r+1 == R else dfs(i+1, r+1, c)
            south = False if r == 0 else dfs(i+1, r-1, c)

            board[r][c] = original
            return east or west or north or south 
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    if dfs(0, r, c): return True
        
        return False
        
        


            

        