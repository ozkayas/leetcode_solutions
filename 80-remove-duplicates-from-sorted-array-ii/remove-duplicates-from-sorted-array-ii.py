class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w,r = 0,0
        hMap = {}

        while r < len(nums):
            hMap[nums[r]] = hMap.get(nums[r], 0) + 1
            if(nums[r] > nums[w]):
                w+=1
                nums[w] = nums[r]
            if(nums[r] == nums[w]):
                if hMap[nums[r]] == 2:
                    w+=1
                    nums[w] = nums[r]



            r+=1


        return w + 1
        