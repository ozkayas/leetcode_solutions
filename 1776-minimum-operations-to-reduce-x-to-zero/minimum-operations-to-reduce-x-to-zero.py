class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # We are trying to find the maximum length subarray with sum of targetSum, ans = N - maxLenSubarray
        targetSum = sum(nums) - x
        if targetSum == 0: return len(nums)

        # will hold preFixSum and indexes {1:0, 2:1, 4:2}, 
        # can not have duplicates because n > 0 and increasing pfSum        
        hMap = dict()
        # to track subarray start:end indexes whose sum is targetSum, there may be more than one subarrays
        # [(0,2)] -> 1 1 4 first example
        subarrays = []
        pfSum = 0
        for i, n in enumerate(nums):
            pfSum += n
            if pfSum == targetSum:
                subarrays.append((0, i))
            elif (pfSum-targetSum) in hMap:
                subarrays.append((hMap[pfSum-targetSum]+1,i))
            hMap[pfSum] = i

        print(subarrays)
        # check the longest subarray of targetSum
        if not subarrays: return -1

        maxSubLen = 0
        for i, j in subarrays:
            maxSubLen = max(maxSubLen, (j-i+1))

        return len(nums) - maxSubLen


             
        