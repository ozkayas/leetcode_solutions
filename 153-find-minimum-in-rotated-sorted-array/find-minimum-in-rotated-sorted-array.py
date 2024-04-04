class Solution:
    def findMin(self, nums: List[int]) -> int:
        #edge cases, if len == 1 or non-rotated
        if  nums[0] <= nums[-1]: return nums[0]


        l , r = 0, len(nums)-1

        while l < r: #not equal , because when we found equal thats the only min value

            mid = (l+r)//2

            # are we on left, or right side
            onLeft = False
            if nums[mid] >= nums[0]:
                onLeft = True

            # there is no target, just crop array until len == 1
            if onLeft: # mid can not be the min, so eliminate it
                l = mid + 1
            else: # we are on the left and maybe mid is the min. so do not eliminate mid
                r = mid


        return nums[l]




'''   


   [4,5,6,7,8,9,,  0,1,2,3] 
            |

// are we on the left or righ tside, compare with the first element  
   
   
'''