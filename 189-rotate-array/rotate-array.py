class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l,r = 0 , len(nums)-1

        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1
        
        l, r = 0, k-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        l, r = k, len(nums)-1
        while l<r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1

        print(nums)






### Solutiion 1
        # res = []
        # i = 0
        # while i < len(nums):
        #     ii = i + len(nums) - k  #i=0 ii=4
        #     ii = ii % len(nums)
        #     # print(ii)
        #     res.append(nums[ii])
        #     i += 1
        
        # for i in range(len(nums)):
        #     nums[i] = res[i]

            