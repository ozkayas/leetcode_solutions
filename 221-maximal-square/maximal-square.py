class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R = len(matrix)
        C = len(matrix[0])

        dp = [[0 for _ in range(C)] for _ in range(R)]
        maxSoFar = 0

        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])
                    maxSoFar = max(maxSoFar, dp[r][c])
                else:
                    cur = matrix[r][c]
                    north = dp[r-1][c]
                    west = dp[r][c-1]
                    nw = dp[r-1][c-1]

                    if cur == "0":
                        dp[r][c] = 0
                    else:
                        dp[r][c] = min(north, west, nw) + 1
                        maxSoFar = max(maxSoFar, dp[r][c])

        return maxSoFar **2

        