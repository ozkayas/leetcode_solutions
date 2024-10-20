class RandomizedSet:

    def __init__(self):
        self.storage = []
        self.table = dict()

    def insert(self, val: int) -> bool:
        if val in self.table: 
            return False
        self.table[val] = len(self.storage)
        self.storage.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.table:
            return False
        idx = self.table[val]
        last = self.storage[-1]
        self.storage[idx] = last
        self.table[last] = idx
        del self.table[val]
        self.storage.pop()
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.storage)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()