class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        blocks = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                cur = board[row][col]
                if cur == ".":
                    continue
                if (cur in rows[row]) or (cur in columns[col]) or (cur in blocks[row//3][col//3]):
                    return False
                else:
                    rows[row].add(cur)
                    columns[col].add(cur)
                    blocks[row//3][col//3].add(cur)
            
        return True
        

'''
create a set for each row, column and block of sudoku
try to fill an empty sudoku and check for uniqness
'''