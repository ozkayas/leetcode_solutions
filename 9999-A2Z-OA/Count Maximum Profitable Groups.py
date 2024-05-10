from typing import List

'''def decreasingQueue(A):


    n = len(A)

    queue = []
    firstLargerToLeft = [-1]*len(A)
    firstLargerToRight = [-1]*len(A)
    firstLargerIndexToLeft = [-1]*len(A)
    firstLargerIndexToRight = [n]*len(A)
    for i,v in enumerate(A):
        while queue and A[queue[-1]] < v:
            k = queue.pop()
            firstLargerToRight[k] = v
            firstLargerIndexToRight[k] = i
            
        if queue:
            firstLargerToLeft[i] = A[queue[-1]]
            firstLargerIndexToLeft[i] = queue[-1]
        queue.append(i)
    return firstLargerToLeft, firstLargerToRight, firstLargerIndexToLeft, firstLargerIndexToRight

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        A = nums 
        _, _, firstLargerIndexToLeft, firstLargerIndexToRight = decreasingQueue(A)
        mark = [0]*(len(A)+1)
        for i in range(len(A)):
            mark[firstLargerIndexToRight[i]] -= 1
            mark[i+1] += 1

        res = [0]*len(A)
        res[0] = mark[0]   
        for i in range(1, len(A)):
            res[i] = res[i-1] + mark[i]
        ans = 1
        for i in range(1, len(A)):
            ans += (i-firstLargerIndexToLeft[i]) + res[i]
        return ans         

print(Solution().numberOfSubarrays(nums= [1,3,1]))

'''


def countSubArray(nums: List[int]) -> int:
    prevGreater = [-1] * len(nums)
    prevNonSmaller = [-1] * len(nums)
    prevNonSmallerCount = [1] * len(nums)

    stack = []
    for (i, num) in enumerate(nums):
        while stack and nums[stack[-1]] <= num:
            stack.pop()
        if stack:
            prevGreater[i] = stack[-1]
        stack.append(i)

    stack = []
    for (i, num) in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            stack.pop()
        if stack:
            prevNonSmaller[i] = stack[-1]
        stack.append(i)

    for i in range(len(nums)):
        if prevNonSmaller[i] >= 0:
            prevNonSmallerCount[i] = 1 + \
                prevNonSmallerCount[prevNonSmaller[i]]

    ans = 0
    for i in range(len(nums)):
        prev = prevGreater[i]
        ans += i - prev
        if prev >= 0:
            ans += prevNonSmallerCount[prev]
    return ans

print(countSubArray([3, 1, 3, 5]), 10)
print(countSubArray([1, 3, 2]), 5)
print(countSubArray([8, 9, 5, 3, 7]), 12)
print(countSubArray([10, 8, 9, 5, 3, 7]), 18)
print(countSubArray([1, 2, 3, 4, 5, 6]), 21)
print(countSubArray([1, 1, 2, 2, 3, 3]), 21)