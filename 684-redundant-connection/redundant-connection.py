class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [ i for i in range(len(edges)+1)]
        rank= [ 1 for i in range(len(edges)+1)]

        print(par)
        print(rank)

        # def find(node):
        #     if par[node] != node:
        #         par[node] = find(par[node])  # Path compression
        #     return par[node]

        def find(node):
            root = node
            while root != par[root]:
                root = par[root]
            
            while root != node:
                nxt = par[node]
                par[node] = root
                node = nxt
                
            return root

        
        def union(n1, n2):
            print("union", n1, n2)
            r1, r2 = find(n1), find(n2)

            if r1 == r2: 
                return True

            if rank[r1] > rank[r2]:
                par[r2] = r1
                rank[r1] += rank[r2]

            else:
                par[r1] = r2
                rank[r2] += rank[r1]
            
            return False

        for n1, n2 in edges:
            if union(n1, n2):
                return [n1, n2]


                
        