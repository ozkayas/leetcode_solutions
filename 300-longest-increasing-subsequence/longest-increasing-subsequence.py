class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        table = [0 for _ in range(len(nums))]
        maxI = len(nums)-1         
        table[maxI] = 1
        i = maxI-1


        while i >= 0:

            maxSeq = 0
            for j in range(i+1, maxI+1):
                if nums[j] > nums[i]:
                    maxSeq = max(maxSeq, table[j])
            table[i] = maxSeq +1

            i -= 1

        return max(table)
            







'''  # RECURSIVE SOLUTION 


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
'''        