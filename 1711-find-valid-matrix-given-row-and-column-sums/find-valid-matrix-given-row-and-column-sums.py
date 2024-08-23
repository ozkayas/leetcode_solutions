class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        R, C = len(rowSum), len(colSum)
        matrix = [[0 for c in range(C)] for r in range(R)]

        r = c = 0
        while r < R and c < C:
            minn = min(rowSum[r],colSum[c])
            matrix[r][c] = minn
            rowSum[r] -= minn
            colSum[c] -= minn
            if rowSum[r] == 0: r += 1
            if colSum[c] == 0: c += 1

        return matrix
