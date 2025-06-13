class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        i, j = 0, N//2
        removed = 0

        while i < N//2 and j < N:
            if nums[i] < nums[j]: 
                i += 1
                removed += 2
            j += 1

        return N - removed 
        