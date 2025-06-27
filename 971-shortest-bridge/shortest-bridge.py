class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R = C = len(grid)
        # find a starting point
        s = None
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    s = [r, c]
                    break
            if s != None: 
                break

        # Mark all cells of the first island with 2
        bfs = deque([s])
        first_island = deque([s])
        while bfs:
            r, c = bfs.popleft()
            grid[r][c] = 2
            for rr, cc in [(r+1,c),(r-1,c),(r,c+1),(r, c-1)]:
                if 0 <= rr < R and 0 <= cc < C:
                    if grid[rr][cc] == 2: continue # Visited
                    if grid[rr][cc] == 1:
                        grid[rr][cc] = 2
                        first_island.append([rr,cc])
                        bfs.append([rr,cc])
        
        # Bfs, and expand the first_island until touching the second island
        level = 0
        while first_island:
            level += 1
            for _ in range(len(first_island)):
                r, c = first_island.popleft()
                for rr, cc in [(r+1,c),(r-1,c),(r,c+1),(r, c-1)]:
                    if 0 <= rr < R and 0 <= cc < C:
                        if grid[rr][cc] == 2: continue # Visited
                        if grid[rr][cc] == 1:
                            return level -1
                        else:
                            grid[rr][cc] = 2
                            first_island.append([rr,cc])








 