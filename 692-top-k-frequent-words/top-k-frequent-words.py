class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mostFreq = 0
        freqs = defaultdict(int)
        for w in words:
            freqs[w] += 1
            mostFreq = max(mostFreq, freqs[w])

        mostFreqSet = set()

        #bucket sort in a list
        bucket = [[] for _ in range(mostFreq+1)]
        for word, freq in freqs.items():
            bucket[freq].append(word)

        print(bucket)

        output = []
        for b in reversed(bucket):
            for word in sorted(b):
                output.append(word)
                if len(output) == k:
                    return output






        