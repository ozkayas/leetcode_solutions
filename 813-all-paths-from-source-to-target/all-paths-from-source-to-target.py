class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        target = len(graph)-1

        def dfs(node, curPath):
            curPath.append(node)
            #base case
            if node == target: 
                res.append(curPath)
                return

            for child in graph[node]:
                dfs(child, curPath.copy())
            

        
        dfs(0, [])

        return res

        