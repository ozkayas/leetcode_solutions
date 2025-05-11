class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        def splitList(nums) -> List[List[int]]:
            output, cur = [], []
            for n in nums:
                if n == 0:
                    if cur:
                        output.append(cur)
                        cur = []
                else:
                    cur.append(n)
            if cur:
                output.append(cur)
            return output
        def maxLenOf(subarr: List[int]) -> int:
            negatives, N = 0, len(subarr)
            for n in subarr:
                if n < 0: negatives += 1
            
            if negatives % 2 == 0:
                return len(subarr)
            else:
                firstLeftNegative, firstRightNegative = 0, N-1
                while subarr[firstLeftNegative] > 0:
                    firstLeftNegative += 1
                while subarr[firstRightNegative] > 0:
                    firstRightNegative -= 1
                # print(firstLeftNegative, firstRightNegative)
                return max(N - firstLeftNegative -1, firstRightNegative) 

        splitted = splitList(nums)

        maxSoFar = 0
        for lst in splitted:
            maxSoFar = max(maxSoFar, maxLenOf(lst))


        return maxSoFar
        