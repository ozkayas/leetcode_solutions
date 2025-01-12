class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k: return False
        odds, evens = 0, 0

        for _ , v in Counter(s).items():
            if v % 2 == 0:
                evens += 1
            else:
                odds += 1

        if odds > k:
            return False

        return True
        