class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        lastProcessed = dict()

        time = 0
        for task in tasks:
            time += 1
            if task not in lastProcessed:
                lastProcessed[task] = time
            else:
                if time - lastProcessed[task] > space:
                    lastProcessed[task] = time
                else:
                    time =  lastProcessed[task]+space + 1
                    lastProcessed[task] = time
                    

        return time

        