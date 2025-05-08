class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # UnionFind solution
        parent = dict()
        for i in range(n):
            parent[i] = i #Assign each as its root

        def find(i:int) -> int:
            root = i

            while root != parent[root]:
                root = parent[root]
            
            # Compression, connect intermediate nodes to root directly as a parent
            cur = i
            while cur != root: # do this until reaching root.
                curParent = parent[cur]
                parent[curParent] = root
                cur = curParent

            return root

        def union(u:int, v:int):
            rootU = find(u)
            rootV = find(v)
            parent[rootV] = rootU

        for u,v in edges:
            union(u,v)
        
        return find(source) == find(destination)

        

        