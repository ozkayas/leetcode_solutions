class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        # In the end, l and r will be boundaries. we will loop while m <= r
        # m is the reader pointer
        # 0 0 0 0 1 1 1 2 2 2 2
        #         l   r

        l, m, r = 0, 0, len(nums)-1

        while m <= r:
            if nums[m] > pivot:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
            elif nums[m] < pivot:
                nums[m], nums[l] = nums[l], nums[m]
                l += 1
                m +=1
            else:
                m += 1
        


        


