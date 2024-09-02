class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        N, counter = len(nums), 0
        nums.sort()
        l, r = 0, (N+1)//2

        while r < N:
            if nums[l]*2 <= nums[r]:
                l += 1 
                r += 1 
                counter += 2
            else:
                r += 1
        
        return counter
            


        