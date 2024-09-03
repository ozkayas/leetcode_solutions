class Solution:
    def splitList(self,lst) -> List[int]:
        result = []
        current = []
    
        for item in lst:
            if item == 0:
                if current:  # current list boş değilse
                    result.append(current)
                    current = []
            else:
                current.append(item)
    
        if current:  # son grup boş değilse onu da ekle
            result.append(current)
    
        return result

    def maxLenOf(self, subarr: List[int]) -> int:
        positives, N = 0, len(subarr)
        for n in subarr:
            if n < 0: positives += 1
        
        if positives % 2 == 0:
            return len(subarr)
        else:
            firstLeftNegative, firstRightNegative = 0, N-1
            while subarr[firstLeftNegative] > 0:
                firstLeftNegative += 1
            while subarr[firstRightNegative] > 0:
                firstRightNegative -= 1
            # print(firstLeftNegative, firstRightNegative)
            return max(N - firstLeftNegative -1, firstRightNegative) 


    def getMaxLen(self, nums: List[int]) -> int:
        maxLen = 0
        subarrays = self.splitList(nums)
        # print(subarrays)

        for subarr in subarrays:
            maxLen = max(maxLen, self.maxLenOf(subarr))
        return maxLen


        