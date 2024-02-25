class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R,C = len(grid),len(grid[0])
        res, counter = [0], [0]

        def dfs(r,c):
            grid[r][c] = 0 #sink the grid
            counter[0] += 1
            res[0] = max(res[0], counter[0])

            for rr,cc in (r+1,c),(r-1,c),(r,c-1),(r,c+1):
                if -1 < rr < R and -1 < cc < C and grid[rr][cc] == 1:
                
                    dfs(rr,cc)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    counter[0] = 0
                    dfs(r,c)
        
        return res[0]