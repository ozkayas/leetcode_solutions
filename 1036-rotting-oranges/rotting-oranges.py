class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C, minutes = len(grid), len(grid[0]), 0
        freshSet, q = set(), []
    
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    freshSet.add((r,c))
                elif grid[r][c] == 2:
                    q.append((r,c,0))
        

        while q:
            r,c,minute = q.pop(0)

            for rr,cc in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if 0<=rr<R and 0<=cc<C and grid[rr][cc] == 1:
                    grid[rr][cc] = 2
                    freshSet.remove((rr,cc,))
                    q.append((rr,cc,minute+1))
                    minutes = minute + 1


        if len(freshSet) > 0:
            return -1
        
        return minutes