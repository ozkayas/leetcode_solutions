class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        listSum = 0
        expectedSum = int(n * (n+1) / 2) 
        for num in nums:
            listSum += num
        
        diff = expectedSum - listSum

        setSum = 0
        s = set(nums)
        for i in s:
            setSum += i
        missingNumber = expectedSum - setSum
        
        return [missingNumber-diff, missingNumber]
