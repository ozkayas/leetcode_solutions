class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)

        pf, result = 0, 0
        for i in range(len(nums)-1):
            pf += nums[i]
            if (pf >= (total-pf)):
                result += 1

        return result