class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        longest = 0
        for k,v in freq.items():
            if k+1 in freq:
                longest = max(longest, freq[k]+freq[k+1])

        return longest

        