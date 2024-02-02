class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return [[]]
        R , C = len(heights), len(heights[0])
        va, vp = set(), set()
        a, p = [], []

        for r in range(R):
            a.append((r, 0))
            p.append((r, C-1))
        for c in range(C):
            a.append((0,c))
            p.append((R-1,c))

        def dfs(r,c,visited):
            visited.add((r,c))
            for rr,cc in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if 0 <= rr < R and 0 <= cc < C and heights[r][c] <= heights[rr][cc] and (rr,cc) not in visited:
                    dfs(rr,cc, visited)

        for r,c in a:
            dfs(r,c,va)
        for r,c in p:
            dfs(r,c,vp)
        
        res = []
        for r,c in va.intersection(vp):
            res.append([r,c])
        
        return res