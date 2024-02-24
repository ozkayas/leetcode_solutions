class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        counter = 0

        def dfs(r,c):
            grid[r][c] = "0"
            
            for rr,cc in (r+1,c),(r-1,c),(r,c+1),(r,c-1):
                if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == "1":
                    dfs(rr,cc)



        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    counter += 1
                    dfs(r,c)

        return counter