class MapSum:

    def __init__(self):
        #buckets for each letter
        self.buckets = [dict() for _ in range(26)]
        
    def insert(self, key: str, val: int) -> None:
        bucketKey = ord(key[0]) - ord("a")
        self.buckets[bucketKey][key] = val

    def sum(self, prefix: str) -> int:
        bucketKey = ord(prefix[0]) - ord("a")
        bucket = self.buckets[bucketKey]
        total = 0
        for k,v in bucket.items():
            if k.startswith(prefix):
                total += v
        return total
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)