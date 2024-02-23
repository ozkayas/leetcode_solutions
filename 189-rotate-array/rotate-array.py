class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        res = []
        i = 0
        while i < len(nums):
            ii = i + len(nums) - k  #i=0 ii=4
            ii = ii % len(nums)
            # print(ii)
            res.append(nums[ii])
            i += 1
        
        for i in range(len(nums)):
            nums[i] = res[i]
            
            