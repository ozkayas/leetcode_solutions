class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseArr(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1

        N = len(nums)
        i = N -2

        # first index from right that brakes the increasing order
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # print(f"index problematic: {i}")

        # All array is in descending order, just reverse the whole array
        if i == -1:
            reverseArr(0, N -1)
            return

        # Find the num just bigger than nums[i]
        k = N -1
        while nums[k] <= nums[i]:
            k -= 1
        
        # print(f"index just bigger than: {k}")
        nums[i], nums[k] = nums[k], nums[i]

        # reverse array from i to the end
        reverseArr(i+1, N -1)


        