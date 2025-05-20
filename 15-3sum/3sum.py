class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        output = []
        i = 0
        for i in range(N-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            target = - nums[i]
            l, r = i+1, N-1
            while l < r:
                total = nums[l]+nums[r]
                if total == target:
                    output.append([nums[i], nums[l], nums[r]])
                    curL, curR = nums[l], nums[r]
                    while nums[l] == curL and l < r:
                        l += 1
                    while nums[r] == curR and l < r:
                        r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1



        return output


        