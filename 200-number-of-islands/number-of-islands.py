class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        islands = 0

        # sink islands using bfs to directions
        def sink(r, c):
            grid[r][c] = "0"

            directions = [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]
            for rr,cc in directions:
                if 0 <= rr < R and 0 <= cc < C and grid[rr][cc] == "1":
                    sink(rr,cc)
        

        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    sink(r,c)
                    islands += 1
        
        return islands
        