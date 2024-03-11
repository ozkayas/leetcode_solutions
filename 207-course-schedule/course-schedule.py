class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        memo = dict()

        # Create Adjacency list
        graph = dict()
        for k,v in prerequisites:
            graph.setdefault(k,[]).append(v)

        # Method detects if a cycle exists
        def hasCycle(node, seen):
            if node in memo:
                return memo[node]

            if node in seen:
                return True
            if node not in graph: 
                return False

            seen.add(node)

            for child in graph[node]:
                if hasCycle(child, seen):
                    memo[child] = True
                    return True
            
            seen.remove(node)
           
            memo[node] = False
            return False



        # Loop over all nodes, because there may be separate graphs
        for n in graph.keys():
            seen = set()
            if hasCycle(n, seen):
                return False

        return True






'''  BFS SOLUTiON , !!!! 

        indeg = [0]*numCourses
        graph = {}
        for u, v in prerequisites:
            indeg[u] += 1
            graph.setdefault(v, []).append(u)

        stack = [i for i, x in enumerate(indeg) if not x]
        seen = []
        while stack:
            x = stack.pop()
            seen.append(x)
            for xx in graph.get(x, []):
                indeg[xx] -= 1
                if indeg[xx] == 0: stack.append(xx)
        return len(seen) == numCourses
''' 