class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        R, C = len(matrix), len(matrix[0])

        dp = [[0 for c in range(C)] for r in range(R)]
        count = 0

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    dp[r][c] = 0
                else:
                    if r == 0 or c == 0:
                        dp[r][c] = matrix[r][c]
                    else:
                        north = dp[r-1][c]
                        west = dp[r][c-1]
                        northWest = dp[r-1][c-1]
                        dp[r][c] = min(north, west, northWest) + 1
                    count += dp[r][c]

        return count