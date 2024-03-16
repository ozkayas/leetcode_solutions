class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)

        for i in range(N):
            minn = nums[i]
            maxx = nums[i]
            for j in range(i+1,N):
                minn = min(minn, nums[j])
                maxx = max(maxx, nums[j])
                res += maxx - minn
        return res