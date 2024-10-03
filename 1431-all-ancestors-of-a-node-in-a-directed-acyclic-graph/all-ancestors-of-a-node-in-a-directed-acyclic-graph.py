class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        ancestors = [[] for _ in range(n)]
        adjList = defaultdict(list)

        for from_node, to_node in edges:
            adjList[from_node].append(to_node)

        def explore(node, parentToAdd):
            for child in adjList[node]:
                if ancestors[child] and ancestors[child][-1] == parentToAdd:
                    continue
                else:
                    ancestors[child].append(parentToAdd)
                    # print(f"visiting {node}, child:{child}, added ancestor{ancestors}")
                    explore(child, parentToAdd)

                
        for node in range(n):
            explore(node, node)

        return ancestors