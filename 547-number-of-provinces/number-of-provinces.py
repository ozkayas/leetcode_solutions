class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        parent = [n for n in range(N+1)]

        # finds the parent/root a node
        def find(n: int) -> int:
            root = n
            while root != parent[root]:
                root = parent[root]

            while n != root:
                next_node = parent[n] 
                parent[n] = root
                n = next_node
        
            return root 

        # bind: parent of v --> u
        def union(u: int, v: int):
            # print(f"union.. {u}, {v}")
            # print(parent)
            rootOfU = find(u)
            rootOfV = find(v)
            parent[rootOfV] = rootOfU
            # print(parent)
        
        # we will union all isConnecteds
        for i in range(N):
            for j in range(i+1, N):
                if isConnected[i][j]:
                    union(i+1, j+1)

        # print(parent)

        for i in range(1, N+1):
            find(i)  # Ensures path compression is applied to all nodes



        # return the set of parents list
        return len(set(parent[1:]))
        