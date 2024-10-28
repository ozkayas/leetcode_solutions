class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        fresh = 0
        bfs = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    bfs.append((r,c)) 
                elif grid[r][c] == 1:
                    fresh +=1

        if not bfs: 
            return 0 if not fresh else -1

        def isValidAndFresh(r,c):
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 1
        
        level = 0
        while bfs:
            for _ in range(len(bfs)):
                r, c = bfs.popleft()
                for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                    if isValidAndFresh(rr,cc):
                        grid[rr][cc] = 2
                        bfs.append((rr,cc))

            level += 1

        # Any remaining fresh after BFS
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return -1
        
        return level-1