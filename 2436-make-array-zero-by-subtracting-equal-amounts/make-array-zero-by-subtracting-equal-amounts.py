class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        uniqueNumsSet = set(nums)
        
        return len(uniqueNumsSet) if 0 not in uniqueNumsSet else len(uniqueNumsSet)-1
        