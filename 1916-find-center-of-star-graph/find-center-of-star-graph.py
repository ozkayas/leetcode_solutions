from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edgeCounter = defaultdict(int)

        for u, v in edges:
            edgeCounter[u] += 1
            edgeCounter[v] += 1

        totalNode = len(edgeCounter)

        for node, edge in edgeCounter.items():
            if edge == totalNode - 1:
                return node

        