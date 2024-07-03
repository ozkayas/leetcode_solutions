class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        diff = float("inf")

        for left in range(4):
            # corresponding right pointer
            right = len(nums) - 4 + left
            diff = min(diff, (nums[right]-nums[left]))

        return diff 
        

'''
 1 2 3 4 5 6 7 8
 l       r
   l       r
     l       r
       l       r
'''