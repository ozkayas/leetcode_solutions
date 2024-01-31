class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = [0]
        counter = [0]
        
        def dfs(r,c):
            # print(r,c)
            grid[r][c] = 0
            counter[0] += 1
            res[0] = max(res[0],counter[0])
            # print('res',res[0])
            for rr,cc in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if 0 <= rr < rows and 0 <= cc < cols and grid[rr][cc] == 1:
                    # print("i", i)
                    dfs(rr,cc)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    counter[0] = 0
                    dfs(r,c)


        return res[0]
