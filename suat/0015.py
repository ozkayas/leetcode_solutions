class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        
        for i in range(len(nums)-2):
            # move i until hitting a new number
            if i != 0 and nums[i] == nums[i-1]:
                continue

            # set 2 pointers for the trailing part after i th index    
            l, r = i+1, len(nums)-1
            target = -1*nums[i]
            while l < r:
                if nums[l]+nums[r] < target:
                    l += 1
                elif nums[l]+nums[r] > target:
                    r -= 1
                else:
                    ans.append([nums[i],nums[l],nums[r]])
                    curL = nums[l]
                    curR = nums[r]
                    while nums[l] == curL and l < r:
                        l += 1
                    while nums[r] == curR and l < r:
                        r -= 1
                
        return ans