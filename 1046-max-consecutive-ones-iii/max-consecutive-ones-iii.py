class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l,r = 0, 0
        # Count 0s and expand window while count < k
        zeros, ans = 0, 0
        while r < N:
            if nums[r] == 0:
                zeros += 1
            if zeros > k:
                ans = max(ans,(r-l))

            # shrink window until zeros is in the limit
            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l +=1
            
            r += 1
        ans = max(ans,(r-l))

        return ans

        