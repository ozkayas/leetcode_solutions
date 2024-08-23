class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Holds the last time we see a preSum % k
        preSumDic = dict()
        preSumDic[0] = -1
        prev = 0

        for i,n in enumerate(nums):
            prev += n
            prev %= k
            # If we see a subset of sum, and length > 1
            if prev in preSumDic:
                if (i - preSumDic[prev]) > 1:
                    return True
            else:
                preSumDic[prev] = i
        
        return False

         