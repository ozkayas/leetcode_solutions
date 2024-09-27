class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def smallerOnLeft(nums: list) -> list:
            # will hold index of the value on left, which is just smaller than this.
            arr = [0] * len(nums)
            stack = [(float("-inf"), -1)] # (value, index)

            for i in range(len(nums)):
                # We need a monotonic increasing stack so pop bigger values
                while stack[-1][0] > nums[i]:
                    stack.pop()
                arr[i] = (stack[-1][1])
                stack.append((nums[i], i))
            return arr
            
        def equalSmallerOnRight(nums: list) -> list:
            # will hold index of the value on left, which is just smaller than this.
            arr = [0] * len(nums)
            stack = [(float("-inf"), len(nums))] # (value, index)

            for i in range(len(nums)-1, -1, -1):
                # We need a monotonic increasing stack so pop bigger values
                while stack[-1][0] >= nums[i]:
                    stack.pop()
                arr[i] = (stack[-1][1])
                stack.append((nums[i], i))
            return arr
            
        def biggerOnLeft(nums: list) -> list:
            # will hold index of the value on left, which is just smaller than this.
            arr = [0] * len(nums)
            stack = [(float("inf"), -1)] # (value, index)

            for i in range(len(nums)):
                # We need a monotonic increasing stack so pop bigger values
                while stack[-1][0] < nums[i]:
                    stack.pop()
                arr[i] = (stack[-1][1])
                stack.append((nums[i], i))
            return arr
            
        def equalBiggerOnRight(nums: list) -> list:
            # will hold index of the value on left, which is just smaller than this.
            arr = [0] * len(nums)
            stack = [(float("inf"), len(nums))] # (value, index)

            for i in range(len(nums)-1, -1, -1):
                # We need a monotonic increasing stack so pop bigger values
                while stack[-1][0] <= nums[i]:
                    stack.pop()
                arr[i] = (stack[-1][1])
                stack.append((nums[i], i))
            return arr

        sumOfMins = 0
        smallOnLeft = smallerOnLeft(nums)
        smallOnRight = equalSmallerOnRight(nums)
        for i, n in enumerate(nums):
            contribution = n * (i-smallOnLeft[i]) * (smallOnRight[i] - i)
            sumOfMins += contribution
            
        sumOfMax = 0
        left = biggerOnLeft(nums)
        right = equalBiggerOnRight(nums)
        for i, n in enumerate(nums):
            contribution = n * (i-left[i]) * (right[i] - i)
            sumOfMax += contribution

        return sumOfMax - sumOfMins 





"""
minSum - ve maxSum of each den ilerlenebilir.
[4,-2,-3,4,1]

min hesabi:
prev kucuk index, next kucuk index
-1.  0    1    2   3   4    5 --> indexler
-inf 4   -2   -3   4   1   -inf --> yeni array
     -1  -1   -1   2   2.        --> first pass left to rigt, < olan indexleri ara
     1    2    5   4   5.        <-- second pass to left, <= olanlari ara


son pass: 
4 x (0 --1) x 1-0.  = 4
-2 X (1--1) X (2-1) = -4
-3 x (2 --1) x (5-2) = -27
4 x (3-2) x (4-3) = 4
1 x (4-2) x (5-4) = 2


"""