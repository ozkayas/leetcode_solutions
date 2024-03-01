class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = Counter(nums)
        # print(counter[0])

        for i in range(len(nums)):
            if counter[0] > 0:
                nums[i] = 0
                counter[0] -= 1
            elif counter[1] > 0:
                nums[i] = 1
                counter[1] -= 1
            else:
                nums[i] = 2