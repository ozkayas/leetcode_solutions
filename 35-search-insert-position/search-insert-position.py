class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        # searching for >= target 
        # [1,3,5,6] 
        #  f t t t

        # edge case if targe > last 
        if target > nums[-1]: return len(nums)

        l, r  = 0, len(nums)-1
        ans = -1

        while l <= r:
            
            m = l + (r-l)//2

            if target <= nums[m]:
                ans = m
                r = m -1
            else:
                l = m +1
        
        return ans

        