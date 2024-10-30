class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1
        R, C = len(grid), len(grid[0])

        def directions(r,c) -> list:
            return [(r-1,c-1),(r-1,c),(r-1,c+1),(r, c+1),(r+1,c+1),(r+1,c),(r+1, c-1),(r,c-1)]
        
        def canVisit(r,c) -> bool:
            return 0 <= r < R and 0 <= c < C and grid[r][c] == 0

        bfs = deque([(0,0)])
        grid[0][0] = 1
        level = 0

        while bfs:
            for _ in range(len(bfs)):
                rr, cc = bfs.popleft()
                if rr == R-1 and cc == C-1:
                    return level+1
                
                for rr,cc in directions(rr,cc):
                    if canVisit(rr,cc):
                        grid[rr][cc] = 1 # visited
                        bfs.append((rr,cc))
            level += 1

        return -1