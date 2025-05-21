class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        rowsToZero = [False for _ in range(R)]
        colsToZero = [False for _ in range(C)]

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    rowsToZero[r] = True
                    colsToZero[c] = True

        for r in range(R):
            for c in range(C):
                if rowsToZero[r] or colsToZero[c]:
                    matrix[r][c] = 0

        
        