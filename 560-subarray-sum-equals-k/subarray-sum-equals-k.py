class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        seen = defaultdict(int)
        pfSum = 0
        for n in nums:
            pfSum += n
            if pfSum == k:
                count += 1
            if (pfSum-k) in seen:
                count += seen[pfSum-k]
            seen[pfSum] += 1


        return count
        