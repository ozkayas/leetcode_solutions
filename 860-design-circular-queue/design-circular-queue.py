class Node:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.lastAdded = None
        self.k = k
        self.len = 0
        # Initialize the circular linked list
        self.root = Node()
        current = self.root
        for _ in range(k - 1):
            current.next = Node()
            current = current.next
        current.next = self.root  # Complete the circle
        self.f = self.root  # Front pointer
        self.r = self.root  # Rear pointer   

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.lastAdded = value # Hold value to reach fast
        self.r.val = value  # Insert value at the rear
        self.r = self.r.next  # Move rear pointer to next node
        self.len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.f.val = None
        self.f = self.f.next
        self.len -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():return -1
        return self.f.val

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.lastAdded

    def isEmpty(self) -> bool:
        return self.len == 0
        

    def isFull(self) -> bool:
        return self.len == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()