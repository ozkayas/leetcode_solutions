class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        ans = []

        for i in range(N-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, N-1
            while l < r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    ans.append([nums[i],nums[l],nums[r]])
                    curL = nums[l]
                    while nums[l] == curL and l < r:
                        l+=1
                    curR = nums[r]
                    while nums[r] == curR and l < r:
                        r-=1

                elif total > 0:
                    r -= 1
                else:
                    l +=1

        return ans
            

        