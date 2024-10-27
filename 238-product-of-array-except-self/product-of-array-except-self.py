class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = [1 for _ in range(N)]
        pre = 1
        for i in range(N):
            ans[i] = pre
            pre *= nums[i]

        pre = 1
        for i in range(N-1, -1, -1):
            ans[i] = ans[i] * pre
            pre *= nums[i]

    
        return ans

        