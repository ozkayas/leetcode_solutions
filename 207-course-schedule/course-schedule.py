class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Kahns Algo:
        orders = []
        # Adjacency list, holds {pre:[course1,course2]} 
        adj = defaultdict(list)
        in_degrees = [0 for _ in range(numCourses)]
        
        ## Fill indegrees list, and adj list
        for course, preReq in prerequisites:
            in_degrees[course] += 1
            adj[preReq].append(course)

        ## Init BFS queue
        bfs_queue = deque()
        # find nodes without pre to start with
        for i, inDegree in enumerate(in_degrees):
            if inDegree == 0:
                bfs_queue.append(i)
        
        while bfs_queue:
            cur = bfs_queue.popleft()

            # put this in orders list and remove if this is a pre for any node indegrees list, 
            orders.append(i)

            # check if there is a cycle
            # If orders > numCourses, this means there is a cycle
            if len(orders) > numCourses:
                return False
            
            # decrese in_degrees for courses from this cur
            for course in adj[cur]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    bfs_queue.append(course)
                


        return len(orders) == numCourses

        
        