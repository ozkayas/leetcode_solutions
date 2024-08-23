class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def fn(cond):
        # """Return topological sort"""
            graph = [[] for _ in range(k)]
            degree = [0]*k
            for u, v in cond:
                graph[u-1].append(v-1)
                degree[v-1] += 1
            queue = deque(u for u, x in enumerate(degree) if x == 0)
            ans = []
            while queue:
                u = queue.popleft()
                ans.append(u+1)
                for v in graph[u]:
                    degree[v] -= 1
                    if degree[v] == 0: queue.append(v)
            return ans
    
        row = fn(rowConditions)
        col = fn(colConditions)

        if len(row) < k or len(col) < k: return []
        ans = [[0]*k for _ in range(k)]
        row = {x : i for i, x in enumerate(row)}
        col = {x : j for j, x in enumerate(col)}
        for x in range(1, k+1): ans[row[x]][col[x]] = x
        return ans