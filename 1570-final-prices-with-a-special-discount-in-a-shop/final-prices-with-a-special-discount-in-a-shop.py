class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []

        for i, p in enumerate(prices):
            if not stack:
                stack.append(i)
            else:
                while stack and prices[stack[-1]] >= p:
                    prices[stack[-1]] -= p
                    stack.pop()
                stack.append(i)
        return prices


"""
monotonik increasin stack from left, stack will hold indexes
[8, 4, 6, 2, 3]
 0
    1
       1,2
          3
             3,4
        
"""
        