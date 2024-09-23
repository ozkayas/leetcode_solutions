class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R, C = len(matrix), len(matrix[0])

        firstColHasZero = False

        # move along row
        for r in range(R):
            if matrix[r][0] == 0: firstColHasZero = True
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        
        print(matrix)
        for r in reversed(range(R)):
            for c in reversed(range(1, C)):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
            if firstColHasZero:
                matrix[r][0] = 0





        