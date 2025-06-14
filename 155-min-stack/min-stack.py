class MinStack:
    Data = namedtuple("Data",["val","minSoFar"])

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(self.Data(val,val))
        else:
            minSoFar = min(self.stack[-1].minSoFar, val)
            self.stack.append(self.Data(val, minSoFar)) 
        

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].minSoFar


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()