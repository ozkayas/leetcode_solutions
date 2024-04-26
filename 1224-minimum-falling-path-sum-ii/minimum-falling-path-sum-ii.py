class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        ans = float("inf")
        R, C = len(grid), len(grid[0])
        memo = dict()

        def dfs(r,c) -> int:
            ## Use cache if available
            if (r,c) in memo:
                return memo[(r,c)]

            ## If base case, return this value
            if r == R-1:
                memo[(r,c)] = grid[r][c]
                return grid[r][c]

            minOfNextLevel = float("inf")
            for cc in range(C):
                if cc != c:
                    minOfNextLevel = min(minOfNextLevel , dfs(r+1, cc))
       
            memo[(r,c)] = int(grid[r][c] + minOfNextLevel)
            return memo[(r,c)]

        for c in range(C):
            ans = min(ans, dfs(0,c))
        
        return ans