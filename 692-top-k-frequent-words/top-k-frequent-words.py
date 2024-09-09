class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        maxCount = 0
        freq = defaultdict(int)
        for w in words:
            freq[w] += 1
            maxCount = max(maxCount, freq[w])

        # filter strings with maxCount freq
        # [(-4, 'the'), (-3, 'is'), (-2, 'sunny'), (-1, 'day')]
        filtered = []
        for w,f in freq.items():
            filtered.append((-f, w))
        filtered.sort()

        ans = [w for f,w in filtered]
        return ans[:k]

        