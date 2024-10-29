class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)

        top, bottom = 0, N-1
        while top < bottom:
            # swap top and bottom rows
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1

        for r in range(N):
            for c in range(r+1, N):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        

        