class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x

        @cache
        def pow_helper(x:float, n:int) -> float:
            if n == 1:
                return x
            half = pow_helper(x, n//2)
    
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half

        return pow_helper(x,n) if n > 0 else 1/pow_helper(x,-n)
        
        