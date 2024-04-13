class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        dp = [[0 for c in range(N+1)] for r in range(M+1)] 
        mx = 0

        for m in range(M):
            for n in range(N):
                if matrix[m][n] == "1":
                    min_of_adj = min(dp[m][n],dp[m][n+1],dp[m+1][n])
                    dp[m+1][n+1] = min_of_adj + 1
                    mx = max(mx, dp[m+1][n+1])

        return mx ** 2
        

        