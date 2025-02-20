class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        limit = 2 ** n # binary nums will be between 0 - limit
        numSet = set()

        for bin_s in nums:
            numSet.add(int(bin_s,2))
        
        for i in range(limit+1):
            if i not  in numSet:
                ans = bin(i)[2:]
                return "0" * (n-len(ans))+ans
        
        return ""
        