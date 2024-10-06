class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        rows = [set() for _ in range(N)]
        cols = [set() for _ in range(N)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur == ".": continue
                else:
                    if cur in rows[r] or cur in cols[c] or cur in blocks[r//3][c//3]:
                        return False
                    else:
                        rows[r].add(cur)
                        cols[c].add(cur)
                        blocks[r//3][c//3].add(cur)

        return True

        