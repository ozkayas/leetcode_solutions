class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # Cycle Sort: put 3 into index:2 , n -> arr[n-1]
        # Then count the nums not in their expected place

        ans = []

        i = 0
        while i < len(nums):
            mustBeIndex = nums[i]-1
            # right number in the place? We are at index i. so the number here should be i+1, if not swap or move i
            if nums[mustBeIndex] != nums[i]: # Num to swaps should be different, if they are same -> infinite loop
                nums[i], nums[mustBeIndex] = nums[mustBeIndex], nums[i]
            else:
                i += 1

        # now the array must be sorted [1,2,3,,,.]
        for i,n in enumerate(nums):
            if i+1 != n:
                ans.append(n)

        return ans



        