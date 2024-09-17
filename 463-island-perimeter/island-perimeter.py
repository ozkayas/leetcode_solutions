class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        edges = 0

        def north(r, c):
            nonlocal edges
            if r == 0 or grid[r-1][c] == 0:
                edges += 1
        def south(r, c):
            nonlocal edges
            if r == R-1 or grid[r+1][c] == 0:
                edges += 1
        def west(r, c):
            nonlocal edges
            if c == 0 or grid[r][c-1] == 0:
                edges += 1
        def east(r, c):
            nonlocal edges
            if c == C-1 or grid[r][c+1] == 0:
                edges += 1

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: 
                    continue
                north(r,c)
                south(r,c)
                west(r,c)
                east(r,c)

        return edges 

