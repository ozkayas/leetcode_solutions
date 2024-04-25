class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        adjList = [[] for _ in range(n)]
        for e in edges:
            u, v = e[0], e[1]
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(v) -> bool:
            visited.add(v)                
            if v == destination:
                    return True

            for u in adjList[v]:
                if u not in visited:
                    if dfs(u):
                        return True
            return False
        
        return dfs(source)

        # visited = set()
        # path = [[] for _ in range(n)]

        # for edge in edges:
        #     path[edge[0]].append(edge[1])
        #     path[edge[1]].append(edge[0])

        # # print(path)
        # def dfs(s) -> int:
        #     # print("s:{}, dest:{}".format(s, destination))
        #     visited.add(s)
        #     if s == destination:
        #         return True
        #     for neigh in path[s]:
        #         if neigh not in visited:
        #             if dfs(neigh):
        #                 return True
            

        #     return False
            



        # return dfs(source)   