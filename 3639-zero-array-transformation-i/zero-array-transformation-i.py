class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        # Difference Array:
        # https://www.youtube.com/watch?v=96RG7EBF8LI
        diffArr = [0 for _ in range(len(nums))]
        for s,e in queries:
            diffArr[s] -= 1
            if e+1 < len(nums):
                diffArr[e+1] +=1
            
        pref = 0

        for i,n in enumerate(diffArr):
            pref += n
            diffArr[i] = pref

        for i in range(len(nums)):
            if nums[i] + diffArr[i] > 0:
                return False

        return True

        