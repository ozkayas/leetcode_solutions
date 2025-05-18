class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        buckets = [0 for _ in range(60)]
        pairs = 0
        for t in time:
            key = t % 60
            pairs += buckets[(60-key)%60]
            buckets[key] += 1 

        return pairs
        
        