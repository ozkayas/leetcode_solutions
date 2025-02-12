class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        maxSoFar = -1
        pairs = defaultdict(list) #digitSum:[nums] -> {9:[18,36], 7:[43,7], 4:[13]} , But we need 2 nums with max value, so we need a heap of 2 items for values, since 2 is a small I will just do simple max comparison

        def sumOfDigits(num: int) -> int:
            sm = 0
            while num:
                lastDigit = num % 10
                num //= 10
                sm += lastDigit
            return sm

        def maxTwo(nums: list[int]) ->int:
            if len(nums) < 3:
                return nums
            else:
                nums.sort()
                return nums[-2:]

        for i, n in enumerate(nums):
            sumN = sumOfDigits(n)
            pairs[sumN].append(nums[i])
            pairs[sumN] = maxTwo(pairs[sumN])
            if len(pairs[sumN]) > 1:
                maxSoFar = max(maxSoFar, sum(pairs[sumN]))

        return maxSoFar

        


        