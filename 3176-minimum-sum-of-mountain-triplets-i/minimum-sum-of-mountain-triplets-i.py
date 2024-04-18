class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N = len(nums)
        found = False
        minSum = 50 * 3

        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1, N):
                    if nums[i] < nums[j] and nums[k] < nums[j]:
                        found = True
                        minSum =  min(minSum, nums[i]+nums[j]+nums[k])

        return minSum if found else -1