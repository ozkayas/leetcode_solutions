class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        N = len(flowerbed)

        def isLeftEmpty(i:int) -> bool:
            return i == 0 or flowerbed[i-1] == 0
        def isRightEmpty(i:int) -> bool:
            return i == N-1 or flowerbed[i+1] == 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and isLeftEmpty(i) and isRightEmpty(i):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True

        return False 