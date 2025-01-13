class Solution:
    def minimumLength(self, s: str) -> int:
        N = len(s)
        freq = [0 for _ in range(26)]
        total = 0

        for i in range(N):
            cur = s[i]
            idx = ord(cur)-ord("a")
            freq[idx] += 1

        for f in freq:
            if f == 0: continue
            if f % 2 == 0:
                total += 2
            else:
                total +=1

        return total

