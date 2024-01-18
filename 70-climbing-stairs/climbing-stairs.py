class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def fn(n:int) -> int:
            if n not in memo:
                val =  fn(n-1) + fn(n-2)
                memo[n] = val
            return memo[n]


        return fn(n)
        

