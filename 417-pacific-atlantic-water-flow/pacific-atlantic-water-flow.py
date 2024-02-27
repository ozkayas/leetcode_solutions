class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M, N = len(heights), len(heights[0])
        pList, aList = [],[]
        pVisited, aVisited = set(), set()
        res = []

        for r in range(M):
            pList.append((r,0))
            aList.append((r,N-1))
        for c in range(N):
            pList.append((0,c))
            aList.append((M-1,c))
    
        def dfs(r,c,visited):
            visited.add((r,c))
            for rr,cc in (r-1,c),(r+1,c),(r,c-1),(r,c+1):
                if -1<rr<M and -1<cc<N and heights[rr][cc] >= heights[r][c] and (rr,cc) not in visited:
                    dfs(rr,cc,visited)
            


        for r,c in pList:
            if (r,c) not in pVisited:
                dfs(r,c,pVisited)

        for r,c in aList:
            if (r,c) not in aVisited:
                dfs(r,c,aVisited)
        
        for r,c in pVisited.intersection(aVisited):
            res.append([r,c])
        
        return res



        