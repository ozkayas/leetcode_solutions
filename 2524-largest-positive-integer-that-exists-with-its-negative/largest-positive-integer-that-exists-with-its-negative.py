class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        s, e = 0, len(nums)-1
        print(nums)
        while nums[e] > 0 and nums[s] < 0:
 
            print("st, end", nums[s], nums[e])
            if nums[s] + nums[e] == 0:
                return nums[e]
            elif abs(nums[e]) > abs(nums[s]):
                e -= 1
            else:
                s += 1
            

        return -1