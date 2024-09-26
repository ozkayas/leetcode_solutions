class FreqStack:

    def __init__(self):
        # hold value and insertion inde
        self.buckets = [[]]
        self.freq = defaultdict(int)

    def push(self, val: int) -> None:
        # Find in which bucket we must push this val
        bucketNo = self.freq[val]
        self.freq[val] += 1
        # Check if this bucket exists in buckests list
        if len(self.buckets) > bucketNo:
            self.buckets[bucketNo].append(val)
        else:
            self.buckets.append([])
            self.buckets[bucketNo].append(val)

    def pop(self) -> int:
        lastBucket = self.buckets[-1]
        popped = lastBucket.pop()
        if not lastBucket:
            self.buckets.pop()
        self.freq[popped] -= 1
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()