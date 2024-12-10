class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banSet = set()
        for x in banned:
            if x <= maxSum:
                banSet.add(x)

        count = 0
        for num in range(1, n+1):
            if num > maxSum:
                break
            if num <= maxSum and num not in banSet:
                count += 1
                maxSum -= num
        return count
        