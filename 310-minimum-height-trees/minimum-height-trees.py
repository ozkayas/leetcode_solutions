class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ## EDGE CASES
        if n == 1: return [0]
        if n == 2: return [0,1]
        
        #create adj list
        adj_list = defaultdict(list)
        #create degrees list
        degrees = [0 for _ in range(n)]
        for edge in edges:
            v, u = edge[0], edge[1]
            adj_list[v].append(u)
            adj_list[u].append(v)
        
        bfs_stack = deque()

        for k,v in adj_list.items():
            degrees[k] = len(adj_list[k])
            ## Filling the leaves at the stack
            if degrees[k] == 1:
                bfs_stack.append(k)

        ## TEST 
        # print(degrees)
        ans = []

        while bfs_stack:
            ans.clear()
            pop_count = len(bfs_stack)

            for _ in range(pop_count):
                leaf = bfs_stack.popleft()
                ans.append(leaf)
                for nei in adj_list[leaf]:
                    degrees[nei] -= 1
                    if degrees[nei] == 1:
                        bfs_stack.append(nei)


        return ans










        