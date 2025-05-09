class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        N = len(nums)
        marked = 0
        l, r = 0, (N+1)//2

        # Two pointer checking
        while r < N :
            if nums[l]*2 <= nums[r]:
                marked += 2
                l += 1
                r += 1
            else:
                r += 1
        return marked

        