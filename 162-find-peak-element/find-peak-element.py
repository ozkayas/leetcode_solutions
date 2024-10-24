class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 4: return nums.index(max(nums))
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1

        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            cur = nums[mid]
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                return mid
            if nums[mid-1] > nums[mid]:
                r = mid-1
            elif nums[mid] < nums[mid+1]:
                l = mid+1
        