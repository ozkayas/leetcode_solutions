class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.memo = dict()


        def dp(r:int, c:int, grid:List[List[int]]) ->int:
            R = len(grid)
            C = len(grid[0])
            if (r,c) in self.memo:
                return self.memo[(r,c)]

            if r == R-1 and c == C-1:
                return grid[r][c]
            east, south = float("inf"), float("inf")
            if c+1 <= C-1:
                east = dp(r, c+1, grid)
            if r+1 <= R-1:
                south = dp(r+1, c, grid)

            curPathSum = grid[r][c] + min(east, south)
            self.memo[(r,c)] = curPathSum
            return curPathSum
        return dp(0, 0, grid)