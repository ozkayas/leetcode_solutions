class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        res = float('inf')
        # find frequencies
        frList = sorted(list(Counter(word).values()))
        for f in frList:
            deleted = 0
            for i in frList:
                if f > i:
                    deleted += i
                elif i > (f+k):
                    deleted += i - (f+k)
            res = min(res, deleted)
        return res
        