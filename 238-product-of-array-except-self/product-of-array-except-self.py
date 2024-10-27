class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        leftProd = [1 for _ in range(N)]
        pre = 1
        for i in range(N):
            leftProd[i] = pre
            pre *= nums[i]
        rightProd = [1 for _ in range(N)]
        pre = 1
        for i in range(N-1,-1,-1):
            rightProd[i] = pre
            pre *= nums[i]

        ans = []
        for i in range(N):
            ans.append(leftProd[i]*rightProd[i])
        
        return ans

        