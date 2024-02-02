class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sides = set()
        visited = set()
        R, C = len(board), len(board[0])

        for r in range(R):
            sides.add((r, 0))
            sides.add((r, C-1))
        for c in range(C):
            sides.add((0, c))
            sides.add((R-1, c))

        # print(sides)

        def dfs(r,c,visited):
            visited.add((r,c))
            for rr,cc in (r-1, c),(r+1, c),(r, c-1),(r,c+1):
                if 0<=rr<R and 0<=cc<C  and board[rr][cc] == "O" and (rr,cc) not in visited:
                    dfs(rr,cc,visited)
        
        for r,c in sides:
            # print("checking side 0 ", r,c)
            # print(board[r][c])
            if board[r][c] == "O":
                # print("found side 0 ", r,c)
                dfs(r,c,visited)
        # print(visited)

        for r in range(R):
            for c in range(C):
                if (r,c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"

        return board

        