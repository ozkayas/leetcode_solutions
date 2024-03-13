class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1 : return 1
        total = (n * (n+1))/2
        preSum = 1
        hMap = {1:1}

        for i in range(2,n+1):
            preSum += i
            hMap[i] = preSum
            if (hMap[i] + hMap[i-1]) == total:
                return i
        
        return -1




'''
        1 + 2 + 3 + 4 + 5 + 6  + 7 + 8
        1.  3.  6. 10   15. 21. 28. 36
'''