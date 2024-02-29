class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.arr.append(val)
            iOfVal = len(self.arr)-1
            self.map[val] = iOfVal
            # print("insert", self.arr, self.map)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.map:
            iOfVal = self.map[val]
            lastItem = self.arr[-1]
            self.map[lastItem] = iOfVal
            self.arr[iOfVal] = lastItem
            del self.map[val]          
            
            self.arr.pop()
            # print("removed", self.arr, self.map)

            return True
        else:
            return False
        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

'''
 0 1 2 3 
[3,1,10,5,]


{3:0, 1:1, 4:2, 10:2}  // val = index
'''