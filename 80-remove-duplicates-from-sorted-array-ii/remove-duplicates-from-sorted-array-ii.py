class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w, r = 0, 0


        while r < len(nums):
            count = 0
            curNum = nums[r]
            while r < len(nums) and nums[r] == curNum:
                r += 1
                count +=1
            
            for _ in range(min(2, count)):
                nums[w] = curNum
                w += 1

        return w

            

        