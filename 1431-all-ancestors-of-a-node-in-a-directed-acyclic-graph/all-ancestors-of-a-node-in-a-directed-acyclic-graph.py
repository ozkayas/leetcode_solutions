class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
            adjList = [[] for i in range(n)]
            inDegree = [0 for i in range(n)]

            for u, v in edges: # u -> v
                adjList[u].append(v)
                inDegree[v] += 1

            
            ans = [[] for i in range(n)]

            ## Fill topological sorting starting nodes
            nodes_with_zero_indegree = deque()
            for i in range(n):
                if inDegree[i] == 0:
                    nodes_with_zero_indegree.append(i)

            topologicalOrder = []
            while nodes_with_zero_indegree:
                curNode = nodes_with_zero_indegree.popleft()
                topologicalOrder.append(curNode)

                for neighbor in adjList[curNode]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        nodes_with_zero_indegree.append(neighbor)
            # Initialize the result list and set list for storing ancestors
            ancestors_list = [[] for _ in range(n)]
            ancestors_set_list = [set() for _ in range(n)]
            
            # Fill the set list with ancestors using the topological order
            for node in topologicalOrder:
                for neighbor in adjList[node]:
                    # Add immediate parent, and other ancestors.
                    ancestors_set_list[neighbor].add(node)
                    ancestors_set_list[neighbor].update(ancestors_set_list[node])

            # Convert sets to lists and sort them
            for i in range(n):
                ancestors_list[i].extend(ancestors_set_list[i])
                ancestors_list[i].sort()

            return ancestors_list


'''
adj List
       0: 3,4
       1: 3
       2: 4, 7
       3: 5,6,7 
       4: 6
       5:
       6:
       7: 
''' 