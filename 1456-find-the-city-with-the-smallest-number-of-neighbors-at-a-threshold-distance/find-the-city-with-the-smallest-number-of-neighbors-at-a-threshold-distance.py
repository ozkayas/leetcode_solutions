class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        """Floyd-Warshall algorithm"""
        dist = [[float("inf")]*n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for i, j, w in edges: dist[i][j] = dist[j][i] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans, ref = 0, inf
        for i in range(n):
            cnt = sum(d <= distanceThreshold for d in dist[i])
            if cnt <= ref: ans, ref = i, cnt
        return ans