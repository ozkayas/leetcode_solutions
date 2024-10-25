class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        # 0 -> 0 : 0
        # 1 -> 1 : 1
        # 0 -> 1 : -1
        # 1 -> 0 : 10
        R, C = len(board), len(board[0])

        def neighbors(r,c)-> int:
            count = 0
            directions = [(r+1,c-1),(r+1,c),(r+1,c+1),(r,c+1),(r-1,c+1),(r-1,c),(r-1,c-1),(r,c-1)]
            for rr,cc in directions:
                if 0 <= rr < R and 0 <= cc < C and board[rr][cc] > 0: # 1 or 10
                    count += 1
            return count

        for r in range(R):
            for c in range(C):
                live_neis = neighbors(r,c)
                if board[r][c] == 1:
                    if live_neis < 2: board[r][c] = 10
                    elif live_neis > 3: board[r][c] = 10
                else:
                    if live_neis == 3: board[r][c] = -1


        for r in range(R):
            for c in range(C):
                if board[r][c] == -1: board[r][c] = 1
                elif board[r][c] == 10: board[r][c] = 0





