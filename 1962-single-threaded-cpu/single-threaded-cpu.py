class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        Task = namedtuple("Task", ["enqTime", "processTime", "id"])
        # Helper method
        def initShortestTaskMinHeap(taskQueue: deque) -> list:
            firstTask = taskQueue.popleft()
            minHeap = [(firstTask.processTime, firstTask.id)]
            return minHeap

        def fillMinHeapWithAvailableTasks(minHeap:list, taskQueue:deque):
            while taskQueue and taskQueue[0].enqTime <= time:
                task = taskQueue.popleft()
                heapq.heappush(minHeap, (task.processTime, task.id))

        sortedTasks = sorted([Task(eTime, pTime, i) for i, [eTime, pTime] in enumerate(tasks)])
        # All the tasks: when simulation time ticks, will take tasks from this queue and add to the procesMinHeap 
        taskQueue = deque(sortedTasks)
        time = taskQueue[0].enqTime
        # Holds tasks with shortest process time enqued in the system, and waiting to be processes, CPU will select from here. not taskQueue
        minHeap = initShortestTaskMinHeap(taskQueue)

        ans = []
        while taskQueue or minHeap:
            # if heap is empty but taskQueue not, means that some taskwill begin in long future, 
            # Fast forward the simulation to the next tasks enque time and re-init minHeap
            if taskQueue and not minHeap:
                time = taskQueue[0].enqTime
                minHeap = initShortestTaskMinHeap(taskQueue)

            # process first task in the heap, then update time and fill heap from taskqueue
            pTime, idx = heapq.heappop(minHeap)
            time += pTime 
            ans.append(idx)
            # Grab the tasks that are now ready to be processed, and push into heap so CPU can select the one with shortest process time
            fillMinHeapWithAvailableTasks(minHeap, taskQueue) 

        return ans


        