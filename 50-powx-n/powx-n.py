class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x

        @cache
        def poww(x:float, n:int) -> float:
            #base cases
            if n == 1: return x

            sub =  poww(x, n // 2)
            if n % 2 == 0:
                return sub * sub
            else:
                return x * sub * sub
            
        return poww(x,n) if n > 0 else 1/poww(x,-n)
        