class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edgesOfNode = defaultdict(int)

        for u, v in roads:
            edgesOfNode[u] += 1
            edgesOfNode[v] += 1

        # list of edges, do no need nodes for the rest of calculations
        # example 1, edgesList = [1, 2 ,2, 3, 4]
        edgesList = sorted(edgesOfNode.values(), reverse = True) 
        # print(edgesList)

        totalImportance = 0
        curAssignValue = n # Start from biggest assignValue, to most edged node, then decrease
        for edgeValue in edgesList:
            totalImportance += curAssignValue * edgeValue
            curAssignValue -= 1

        return totalImportance




        