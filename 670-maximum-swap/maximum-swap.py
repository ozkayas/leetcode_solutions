class Solution:
    def maximumSwap(self, num: int) -> int:
        Max = namedtuple("Max", ["value", "index"])
        
        numList = [int(ch) for ch in str(num)]
        N = len(numList)

        # holds Max(value, index)
        maxOnRight = [Max(0,N) for _ in range(N)] # [Max, Max] 
        maxOnRight[-1] = Max(numList[-1], N-1) 
        for i in range(N-2, -1, -1):
            if numList[i] > maxOnRight[i+1].value:
                maxOnRight[i] = Max(numList[i],i)
            else:
                maxOnRight[i] = maxOnRight[i+1]

        # Second pass from left, swap as soon as finding a max value greter than this
        for i,n in enumerate(numList):
            if n < maxOnRight[i].value:
                j = maxOnRight[i].index
                numList[i], numList[j] = numList[j], numList[i]
                return int("".join([str(num) for num in numList]))

        
        return int("".join([str(n) for n in numList]))





        


"""
1st pass:
right to left, hold maxSoFar and index of it
2nd pass:
mx =  
273619 
     i



"""