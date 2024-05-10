class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        N  = len(happiness)

        happiness.sort(reverse = True)

        total = 0

        for i, h in enumerate(happiness[:k]):
            total += max(h-i, 0)
        return total