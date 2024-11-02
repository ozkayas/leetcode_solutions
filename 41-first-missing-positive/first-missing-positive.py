class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cycle sort = iterate nums and put them in their must-be position
        # 1 -> must be at index[0]
        # 2 -> must be at index[1]
        # n -> must be at index[n-1]
        N = len(nums)
        i = 0
        while i < N:
            mustBeIdx = nums[i]-1
            if 0 < nums[i] <= N and nums[i] != nums[mustBeIdx]:
                nums[mustBeIdx], nums[i] = nums[i], nums[mustBeIdx]
            else:
                i += 1
                

        print(nums)

        for i, n in enumerate(nums):
            if i+1 != n:
                return i+1

        return N+1

        