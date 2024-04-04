class TimeMap:

    def __init__(self):
        self.store = dict() # {key: [(time_stamp,value1),(time_stamp,value2)]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(timestamp,value)]
        else:
            self.store[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store: return ""

        values_of_key = self.store[key]
        if timestamp < values_of_key[0][0]: return ""

        l, r = 0, len(values_of_key)-1
        
        while l <= r:
            mid = (l+r)//2
            cur = values_of_key[mid]

            if cur[0] == timestamp:
                return cur[1]
            elif timestamp < cur[0]:
                r = mid -1
            else:
                l = mid + 1
            
        return values_of_key[r][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
