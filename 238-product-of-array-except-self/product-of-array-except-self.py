class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# This is the easiest way but requires extra space,
# The point is while creating preFixSum or preFixProduct we have 2 options
# 1 -> Use and then reCalculte preFix
# 2 -> Recalculte and then Use preFix

        N = len(nums)
        lProd = [1 for _ in range(N)]
        rProd = [1 for _ in range(N)]
        ans = []
        pFix, sFix = 1, 1
        
        for i in range(N):
            lProd[i] = pFix
            pFix *= nums[i]

        for i in range(N-1,-1,-1):
            # rProd[i] = sFix  # Instead of a newArr we can write on the lProd and just return it as optimal solution
            lProd[i] = lProd[i] * sFix
            sFix *= nums[i]


        for i in range(N):
            ans.append(lProd[i]*rProd[i])

        return ans
            
'''
        ans = [1] * len(nums)
        prefix = suffix = 1
        for i in range(len(nums)):
            ans[i] *= prefix 
            ans[-i-1] *= suffix 
            # print(i, ~i)#
            # print(ans[i], ans[~i])#
            prefix *= nums[i]
            suffix *= nums[-i-1]
        return ans
'''
'''
        res = [1 for _ in range(len(nums))]
        tempProd = 1

        #First pass
        for i in range(len(nums)):
            res[i] *= tempProd
            tempProd *= nums[i]

          #Second pass
        tempProd = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= tempProd
            tempProd *= nums[i]

        return res
'''




        # for i, num in enumerate(nums):
        #     arr[i] = pre
        #     pre = pre * num
        #     print(arr)
        # for i in range(len(nums)-1, -1, -1):
        #     arr[i] *= post
        #     post = post * nums[i]
        #     print(arr) 
        # return arr   

'''
# First Pass
1,2,3,4
1,1,1,1
*

1,2,3,4
1,1,1,1
  *

1,2,3,4
1,1,2,1
    *

1,2,3,4
1,1,2,6
      *   

# Second Pass
1,2,3,4
1,1,8,6
    *
1, 2,3,4
1,12,8,6
  *
 1, 2,3,4
24,12,8,6
*




'''
