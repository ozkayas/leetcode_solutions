class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix, ans = 0, 0
        seen = {0:1}

        for n in nums:
            prefix += n
            ans += seen.get(prefix - goal, 0)
            seen[prefix] = 1 + seen.get(prefix, 0)
            
        return ans

        