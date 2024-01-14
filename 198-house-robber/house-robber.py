class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        N = len(nums)-1
        if N == 0: return nums[0]
        if N == 1: return max(nums[0], nums[1])

        def fn(i):
            if i in memo:
                return memo[i]
            

            if i == N:
                return nums[N]
            if i == N-1:
                return max(nums[N-1], nums[N])
            
            memo[i] = max(  nums[i]+fn(i+2) , fn(i+1) )
            return memo[i]


        return fn(0)


        