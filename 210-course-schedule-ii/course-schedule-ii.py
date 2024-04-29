class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list) ## ajd[prereq] = [courses...]
        orders = []
        in_degrees = [0 for _ in range(numCourses)] ## in_degrees[course] = count of preReqs/indegrees

        for course, preReq in prerequisites:
            adj[preReq].append(course)
            in_degrees[course] += 1

        bfs_q = deque()
        for course, indegree in enumerate(in_degrees):
            if indegree == 0:
                bfs_q.append(course)
        
        while bfs_q:
            cur = bfs_q.popleft()

            orders.append(cur)

            #check if cycle exists
            if len(orders) > numCourses:
                return []
            
            # Remove cur from indegrees list
            for course in adj[cur]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0: # There is no in_degree/preRef for this course now, so add to the queue
                    bfs_q.append(course)


        return orders if len(orders) == numCourses else []
        