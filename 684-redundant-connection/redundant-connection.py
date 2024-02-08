class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [ i for i in range(len(edges)+1)]
        rank= [ 1 for i in range(len(edges)+1)]

        print(par)
        print(rank)

        def find(n):
            root = n
            while root != par[root]: # not at the top, root 
                root = par[root]
            return root
        
        def union(n1, n2):
            print("union", n1, n2)
            r1, r2 = find(n1), find(n2)

            if r1 == r2: 
                return False

            if rank[r1] > rank[r2]:
                par[r2] = r1
                rank[r1] += rank[r2]

            else:
                par[r1] = r2
                rank[r2] += rank[r1]
            
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]


                
        