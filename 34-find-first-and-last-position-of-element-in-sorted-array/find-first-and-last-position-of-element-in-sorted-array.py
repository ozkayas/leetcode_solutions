class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        idx = -1
        res = [-1, -1]

        #First binary search to catch any index of target, or return -1 and finish search
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] == target:
                idx = m
                break
            if target < nums[m]:
                r = m -1
            else:
                l = l +1

        if idx == -1:
            return res
        
        #Second binary search to detect start of the target
        l, r = 0, idx
        ans = -1
        while l <= r:
            m = l + (r-l)//2

            if target <= nums[m]:
                ans = m
                r = m - 1
            else:
                l = m + 1

        res[0] = ans

        # Third binary search to detect the ending of the target
        l, r = idx, len(nums)-1
        ans = -1
        print(nums[idx:])
        while l <= r:
            m = l + (r-l)//2

            if target >= nums[m]:
                ans = m
                l = m + 1
            else:
                r = m - 1

        res[1] = ans


        return res

    
'''
#second binary search
 t t t f f f   <- find first false
[5,7,7,8,8,8]
       ^

#third binary search
 t t t t f f   <- find last true
[8,8,8,8,9,10]
     ^
'''