class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()
        provinces = 0

        def dfs(i:int):
            visited.add(i)
            # loop on neighs
            for j in range(N):
                if i != j and isConnected[i][j] and (j not in visited):
                    dfs(j)
                    

        
        for i in range(N):
            if i not in visited:
                provinces += 1
                dfs(i)

        return provinces

        