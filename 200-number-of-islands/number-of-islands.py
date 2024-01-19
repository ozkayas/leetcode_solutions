class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        count = 0

        def dfs(r,c):
            visited.add((r,c))
            #check N
            if r -1 >= 0 and grid[r-1][c] == "1" and (r-1,c) not in visited:
                dfs(r-1,c)
            #check S
            if r +1 <= rows-1 and grid[r+1][c] == "1" and (r+1,c) not in visited:
                dfs(r+1,c)
            #check E
            if c+1 <= cols-1 and grid[r][c+1] == "1" and (r,c+1) not in visited:
                dfs(r,c+1)
            #check w
            if c -1 >= 0 and grid[r][c-1] == "1" and (r,c-1) not in visited:
                dfs(r,c-1)
    

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c] == "1":
                    count+= 1
                    dfs(r,c)
        

        return count