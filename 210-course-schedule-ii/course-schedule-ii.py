class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj = defaultdict(list)
        inDeg = [0 for _ in range(numCourses)]

        for to, fr in prerequisites:
            adj[fr].append(to)
            inDeg[to] += 1
        
        bfsQ = deque()
        for i in range(numCourses):
            if inDeg[i] == 0:
                bfsQ.append(i)
        
        while bfsQ:
            for _ in range(len(bfsQ)):
                cur = bfsQ.popleft()
                order.append(cur)
                # update indeg table
                for nei in adj[cur]:
                    inDeg[nei] -= 1
                    if inDeg[nei] == 0:
                        bfsQ.append(nei)

        return order if len(order)==numCourses else []

        