class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited  = set()
        numberOfProvinces = 0

        def dfs(i: int):
            visited.add(i)
            print("i:", i, "vis:", visited, "neighbors of this:",isConnected[i])
            for j in range(N):
                if isConnected[i][j] == 1 and j not in visited: # <- if there is a connection
                    dfs(j)
                    
        for i in range(N):
            if i not in visited:
                numberOfProvinces += 1
                dfs(i)

        return numberOfProvinces