class Solution:
    def check(self, nums: List[int]) -> bool:
        decreaseCount = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                decreaseCount += 1
            if decreaseCount > 1:
                return False

        if nums[0] < nums[-1] and decreaseCount: 
            return False

        return True

        