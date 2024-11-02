class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.table:
            return ""
        
        values = self.table[key]
        if timestamp < values[0][0]: return ""
        if timestamp > values[-1][0]: return values[-1][-1]


        targetIdx = bisect_left(values, (timestamp,))
        
        # if timestamp exists return that index, else return the previous  
        if values[targetIdx][0] == timestamp:
            return values[targetIdx][1]
        else:        
            return values[targetIdx-1][1]

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
