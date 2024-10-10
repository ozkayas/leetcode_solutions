class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        Num = namedtuple("Num", ["val", "idx"])
        nums = sorted([Num(n,i) for i, n in enumerate(nums)])

        minIdxSoFar = nums[0].idx
        maxW = 0

        for i in range(1, len(nums)):
            if nums[i].idx >= minIdxSoFar:
                maxW = max(maxW, nums[i].idx - minIdxSoFar)
            
            minIdxSoFar = min(minIdxSoFar, nums[i].idx)

        return maxW

        