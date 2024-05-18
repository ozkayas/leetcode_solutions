from collections import defaultdict
from heapq import heappush, heappop

class Lazyheap:
    """Maintains a heap where elements can be removed.
    Elements do not have to be distinct.
    Removals are done in lazy manner, namely only when seen at top.
    toremove[v] = how many times v has yet to be removed.
    """
    def __init__(self):
        self.h = []  # the actual heap
        self.n = 0   # number of (non removed) items in heap
        # self.sum = 0 # their sum
        self.toremove = defaultdict(int)
    
    def push(self, item):
        heappush(self.h, item)
        self.n += 1
        # self.sum += item

    def remove(self, item):
        # just mark for later actual removal
        self.toremove[item] += 1    
        self.n -= 1
        # self.sum -= item

    def top(self):
        """returns smallest (non removed) item of heap"""
        x = self.h[0]
        while self.toremove[x] > 0:
            self.toremove[x] -= 1
            heappop(self.h)
            x = self.h[0]
        return x

    def pop(self):
        """ removes and returns smallest element """
        x = self.top()
        heappop(self.h)
        self.n -= 1
        # self.sum -= x
        return x


lHeap = Lazyheap()

lHeap.push(3)
lHeap.push(3)
lHeap.push(2)
lHeap.push(1)
lHeap.remove(3)
lHeap.remove(1)
lHeap.pop()
lHeap.pop()