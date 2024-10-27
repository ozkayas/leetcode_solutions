class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        inDegrees = [0 for _ in range(numCourses)]
        
        for to, fr in prerequisites:
            adj[fr].append(to)
            inDegrees[to] += 1
        
        bfsQ = deque()
        # find nodes without pre to start with
        for i, inDegree in enumerate(inDegrees):
            if inDegree == 0:
                bfsQ.append(i)
    
        courses_order = []
        while bfsQ:
            cur = bfsQ.popleft()
            courses_order.append(cur)
             
            # if len(courses_order) > numCourses: return False
            
            #update inDegrees
            for nei in adj[cur]:
                inDegrees[nei] -= 1
                if inDegrees[nei] == 0:
                    bfsQ.append(nei)
        return len(courses_order) == numCourses