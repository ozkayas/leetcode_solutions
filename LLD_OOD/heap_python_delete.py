import itertools
import heapq

class HeapX:
    def __init__(self) -> None:
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = '<removed-task>'           # placeholder for a removed task
        self.counter = itertools.count()     # unique sequence count

    def add_task(self, task, priority=0):
        # 'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.remove_task(task)
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)

    def remove_task(self,task):
        # 'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def pop_task(self):
        # 'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heapq.heappop(self.pq)
            if task is not self.REMOVED:
                del self.entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')
    
# h = HeapX()
# h.add_task(5)
# h.add_task(7)
# h.add_task(1)
# h.remove_task(5)
# h.pop_task()



#### SIMPLEST IMPLEMENTATION 
class LazyDeleteHeap:
    def __init__(self):
        self.heap = []
        self.deleted = set()  # Set kullanarak silinen elemanları izleyeceğiz

    def push(self, item):
        heapq.heappush(self.heap, item)

    def remove(self, item):
        self.deleted.add(item)

    def pop(self):
        while self.heap[0] in self.deleted:  # En küçük elemanı alırken  silinenleri atlayacağız
            heapq.heappop(self.heap)
        return heapq.heappop(self.heap)

    def peek(self):
        top_element = self.heap[0]
        while top_element in self.deleted:
            heapq.heappop(self.heap)
            top_element = self.heap[0]
        return top_element


    def __len__(self):
        return len(self.heap) - len(self.deleted)

nums = [ 3, 4, 1, 1, 5, 9]
heapq.heapify(nums)
removed = set()

print(nums)

# Removing 1
removed.add(1)

while nums
