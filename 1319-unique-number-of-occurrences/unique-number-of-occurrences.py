class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        s = set()

        for key, val in counter.items():
            s.add(val)

        return len(s) == len(counter)

        