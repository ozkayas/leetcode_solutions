class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            cur = n
            while (cur-1) in numSet:
                cur -= 1
            count = 0
            while (cur in numSet):
                numSet.remove(cur)
                count += 1
                cur += 1
            longest = max(longest, count)
        return longest
            

        