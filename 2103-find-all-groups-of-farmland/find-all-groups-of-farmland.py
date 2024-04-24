class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        res = []
        R, C = len(land), len(land[0])
        ## I had to use visited set because we got memory limit exceeded error, just turning 1 -> 0 does not quarantee 
        visited = set()

        def bfs(r,c):
            visited.add((r,c))
            q = deque()
            q.append((r,c))

            while len(q) > 0:
                r, c = q.popleft()
                land[r][c] = 0

                # Check if corner or on the edge of tha land
                if (r == R-1 or land[r+1][c] == 0) and (c == C-1 or land[r][c+1] == 0):
                    res[-1].append(r)
                    res[-1].append(c)
                    return
            
                if r+1 < R and land[r+1][c] == 1 and (r+1,c) not in visited:
                    visited.add((r+1,c))
                    q.append((r+1,c))
                if c+1 < C and land[r][c+1] == 1 and (r,c+1) not in visited:
                    visited.add((r,c+1))
                    q.append((r,c+1))

        for r in range(R):
            for c in range(C):
                if land[r][c] == 1 and (r,c) not in visited:
                    res.append([r,c])
                    bfs(r,c)
        
        return res
        