class Solution:
    def isHappy(self, n: int) -> bool:
        bucket = set() # Keep track of the calculated sumOfSquares

        def sumOfSqr(num: int) -> int:
            digits = []
            sum = 0
            while num > 0:
                lastDigit = num % 10
                sum += lastDigit **2
                num = num // 10
            
            return sum
        
        curSumOfSq = n
        bucket.add(n)

        while curSumOfSq != 1: #Trying to reach a happy number
            curSumOfSq = sumOfSqr(curSumOfSq)
            if curSumOfSq in bucket:
                return False
            else:
                bucket.add(curSumOfSq)
        
        return True
