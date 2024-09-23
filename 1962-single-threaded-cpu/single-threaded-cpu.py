class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        sortedTasks = sorted([(eTime, pTime, i) for i, [eTime, pTime] in enumerate(tasks)])
        # print(sortedTasks)
        taskQueue = deque(sortedTasks)

        # init minHeap with the first value
        firstTask = taskQueue.popleft()
        time = firstTask[0]
        minHeap = [(firstTask[1],firstTask[2])]
        heapq.heapify(minHeap)

        ans = []
        while taskQueue or minHeap:
            # if heap is empty but taskQueue not, means that some taskwill begin in long future, but heap is processed
            if taskQueue and not minHeap:
                firstTask = taskQueue.popleft()
                time = firstTask[0]
                minHeap = [(firstTask[1],firstTask[2])]
                heapq.heapify(minHeap)

            # process first task in the heap, then update time and fill heap from taskqueue
            pTime, idx = heapq.heappop(minHeap)
            time += pTime 
            ans.append(idx)
            # print(f"found time{time}, pTime{pTime}, idx:{idx}")
            # popleft from queue until time, and push into heap
            while taskQueue and taskQueue[0][0] <= time:
                task = taskQueue.popleft()
                heapq.heappush(minHeap, (task[1], task[2]))


        return ans


        