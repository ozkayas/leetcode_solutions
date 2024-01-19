class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows-2, -1, -1):
            for c in range(cols):
                if c == 0:
                    matrix[r][c] += min(matrix[r+1][c],matrix[r+1][c+1])
                elif c == cols-1:
                    matrix[r][c] += min(matrix[r+1][c-1],matrix[r+1][c])
                else:
                    matrix[r][c] += min(matrix[r+1][c-1],matrix[r+1][c],matrix[r+1][c+1])
                    
        res = matrix[0][0]

        for n in matrix[0]:
            res = min(res, n)

        return res

        