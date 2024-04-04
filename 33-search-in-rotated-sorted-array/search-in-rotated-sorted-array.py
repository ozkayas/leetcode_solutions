class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == nums[-1] and nums[0] == target: return 0

        l, r = 0 , len(nums)-1

        while l <= r:
            mid = (l+r)//2
            cur = nums[mid]
            if target == cur:
                return mid

            onLeft = True if cur >= nums[0] else False

            if onLeft:
                if target > cur:
                    l = mid + 1
                else:
                    if target >= nums[0]: # target on the left
                        r =  mid - 1
                    else:
                        l = mid + 1
            else:
                if target < cur:
                    r = mid - 1
                else:
                    if target <= nums[-1]: # target on the right
                        l = mid + 1
                    else:
                        r = mid - 1
            
        return -1
        
        