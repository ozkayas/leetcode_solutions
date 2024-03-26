class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)

        i = 1
        while True:
            if i in s:
                s.remove(i)
                i += 1
            else:
                return i
        
        