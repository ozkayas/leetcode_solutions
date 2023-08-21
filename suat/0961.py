class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        set1 = set()

        for num in nums:
            if num in set1:
                return num
            else:
                set1.add(num)