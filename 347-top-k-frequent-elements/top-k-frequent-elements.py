class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        maxFreq = max(freq.values())
        # Each index of the bucket represents elements with the corresponding frequency
        bucket = [[] for _ in range(maxFreq+1)]

        for key, v in freq.items():
            bucket[v].append(key)

        ans = []
        while k > 0 and bucket:
            keys = bucket.pop()
            ans.extend(keys)
            k -= len(keys)

        return ans