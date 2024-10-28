class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # if len(nums) == 1 and 
        def isOnLeft(idx:int):
            return nums[idx] >= nums[0]
        def isOnRight(idx:int):
            return nums[idx] <= nums[-1]

        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = lo + (hi-lo)//2
            if nums[mid] == target: return mid

            if isOnLeft(mid):
                if nums[0] <= target < nums[mid]: #target on left
                    hi = mid -1
                else:
                    lo = mid + 1  
            elif isOnRight(mid):
                if nums[mid] < target <= nums[-1]: #target on right
                    lo = mid + 1  
                else:
                    hi = mid -1
            else:
                return -1

        return -1
        