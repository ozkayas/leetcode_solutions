class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #Edge cases
        if nums[0] > 0 or nums[-1] < 0:
            return []
        
        N = len(nums)
        ans = set()

        for i in range(N-2):
            lo , hi = i+1, N-1          
            while lo < hi:
                sm = nums[i] + nums[lo] + nums[hi]
                if sm == 0:
                    ans.add((nums[i],nums[lo],nums[hi]))
                    lo +=1
                    
                elif sm < 0:
                    lo +=1
                else:
                    hi -= 1
        
        ansList = []
        for item in ans:
            ansList.append([item[0],item[1],item[2]])
        
        return ansList



        