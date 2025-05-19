class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        parent = dict()
        for i in range(N):
            parent[i] = i

        def find(i:int) -> int: # returns parent/root
            pointer = i
            while parent[pointer] != pointer:
                pointer = parent[pointer]

            root = pointer
            pointer = i
            while pointer != root:
                pointerParent = parent[pointer]
                parent[pointer] = root
                pointer = pointerParent
            
            return root
        
        def union(u:int, v:int):
            rootU = find(u)
            rootV = find(v)
            parent[rootV] = rootU

        for i in range(N):
            for j in range(i+1,N):
                if isConnected[i][j] == 1:
                    union(i,j)

        roots = set()
        for i in range(N):
            roots.add(find(i))

        return  len(set(roots))

        