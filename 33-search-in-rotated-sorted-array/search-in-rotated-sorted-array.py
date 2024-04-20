class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 1:
            return 0 if nums[0]==target else -1

        l, r = 0, len(nums)-1
        
        while l <= r:
            ans = -1
            m = l + (r-l)//2

            if nums[m] == target: return m

            # On the left portion? 
            if nums[m] > nums[-1]:
                if nums[0] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # on the right portion
                if nums[m] < target <= nums[-1]: # target is also on the right portion
                    l = m + 1
                else:
                    r = m - 1
        return ans
        
        

'''        while l <= r:
            
            # print(f"beginning loop with {nums[l:r+1]}")
            i = (l+r)//2
            if nums[i] == target: # if we hit the target
                return i

            if nums[0] <= nums[i]: # on the left portion
                if nums[i] < target: 
                    l = i +1 # crop left of i
                else:
                    if nums[0] <= target:
                        r = i -1
                    else:
                        l = i +1 # crop left of i

            if nums[0] >= nums[i]: # on the right portion
                if target < nums[i]: 
                    r = i -1 # crop right of i
                else:
                    if target <= nums[-1]:
                        l = i +1
                    else:
                        r = i -1 
                    
        return -1'''