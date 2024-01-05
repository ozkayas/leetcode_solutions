class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}
        i, maxI =0, len(nums)-1
        res = 0

        def fn(i) -> int:
            # print("i:{}, memo:{}".format(i,memo))
            if i == maxI:
                return 1

            if i in memo:
                return memo[i]

            maxChild = 0

            for j in range(i+1,maxI+1):
                
                if nums[i] < nums[j]:
                    val = fn(j)
                    maxChild = max(maxChild, val)

            
            memo[i] = 1 + maxChild
            return 1 + maxChild


        while i <= maxI:
            res = max(res, fn(i))
            i+=1

        return res
        