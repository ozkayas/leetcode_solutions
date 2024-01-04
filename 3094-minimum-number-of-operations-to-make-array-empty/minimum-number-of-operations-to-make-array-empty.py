class Solution:
    def minOperations(self, nums: List[int]) -> int:
        f = Counter(nums)
        memo = {}

        def backT(n:int) -> int:
            if n == 2 or n == 3: return 1
            if n == 0: return 0
            if n == 1: return -1
            if n in memo:
                return memo[n]
            
            r = backT(n-3)
            r = float('inf') if r == -1 else r
            
            l = backT(n-2)
            l = float('inf') if l == -1 else l

            memo[n] = min(l , r) + 1
            return memo[n]
        

        totalSteps = 0
        for num in f:
            step = backT(f[num])
            if step == -1:
                return -1
            else:
                totalSteps += step
        return totalSteps




        # print(0, backT(0))    
        # print(1, backT(1))    
        # print(2, backT(2))    
        # print(3, backT(3))    
        # print(4, backT(4))    
        # print(5, backT(5))           
        # print(6, backT(6))    
        # print(7, backT(7))    
        # print(8, backT(8))    
        # print(9, backT(9))    

''' left branch -2, right branch -3
         5
        / \
       3   2
      /\   /\
     1  0 0  -1


'''