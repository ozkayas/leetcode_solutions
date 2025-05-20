class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(C)] for _ in range(R)]

        for r in range(R):
            for c in range(C):
                if r == 0 or c == 0:
                    dp[r][c] = int(matrix[r][c])
                elif matrix[r][c] == "0":
                    continue
                else:
                    north, west, nw = dp[r-1][c], dp[r][c-1], dp[r-1][c-1]
                    dp[r][c] = min(north, west, nw) +1
        maxx = 0
        for r in range(R):
            for c in range(C):
                maxx = max(maxx, dp[r][c])
                
        return maxx ** 2
        