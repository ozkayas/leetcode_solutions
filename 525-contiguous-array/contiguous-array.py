class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        hMap = {0:[-1]}
        preFix = 0
        ans = 0

        for i,n in enumerate(nums):
            preFix += 1 if n == 1 else (-1)
            hMap[preFix] = hMap.get(preFix,[]) + [i]
            #update ans
            ans = max(ans, (hMap[preFix][-1] - hMap[preFix][0]))
        return ans

        
'''
       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1,] 
        -1 0 -1 -2  -1 0  -1 -2 -1 0 

        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1,] 
        -1 -2 -3 -4 -5 -4 -5 -6 -5 -4
        
        -1 : [0]
        -2 : [1]
        -3 : [2]
        -4 : [3,5,9]
        -5 : [4,6,8]
        -6 : [7]


'''