class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 and c == 0 and obstacleGrid[r][c] == 0:
                    dp[r][c] = 1
                    continue
                if obstacleGrid[r][c] == 1:
                    dp[r][c] = 0
                else:

                    leftState = dp[r][c-1] if c-1 >=0 else 0
                    topState = dp[r-1][c] if r-1 >=0 else 0
                    dp[r][c] = leftState + topState 
    

        return dp[m-1][n-1]