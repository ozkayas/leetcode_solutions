class MinStack:
    StackData = namedtuple("StackData", ["val", "minSoFar"])

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack: 
            self.stack.append(self.StackData(val, val))
        else:
            minSoFar = min(val, self.stack[-1].minSoFar)
            self.stack.append(self.StackData(val, minSoFar))
        
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