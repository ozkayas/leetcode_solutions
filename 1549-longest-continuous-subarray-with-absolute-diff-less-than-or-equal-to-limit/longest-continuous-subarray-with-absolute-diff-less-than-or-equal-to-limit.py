from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 0
        sl = SortedList()
        ans = 0

        while r < len(nums):
            sl.add(nums[r])
            # Check if window is valid or not
            mn, mx = sl[0], sl[-1]
            if abs(mx-mn) <= limit:
                ans = max(ans, (r-l+1))
            
            # Shrink window until reaching a valid state  
            while abs(mx-mn) > limit:
                sl.remove(nums[l])
                l += 1
                # Update min and max since `l` was modified
                mn, mx = sl[0], sl[-1] if sl else (0, 0)

            r += 1
        
        return ans


        