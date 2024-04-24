class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Searching for x >= target question, searching for the index actually
        l, r = 0, len(nums)-1
        idx = -1

        if target > nums[-1]:
            return len(nums)

        while l <= r:
            m = l + (r-l)//2

            if target <= nums[m]:
                idx = m
                r = m - 1
            else:
                l = m + 1
        
        return idx

        