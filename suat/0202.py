class Solution:
    def isHappy(self, n: int) -> bool:
        #helper function
        def sumOfSq(n:int) -> int:
            return sum(int(i)**2 for i in str(n))

        if sumOfSq(n) == 1:
            return True
        
        slow, fast = n, n
        while (fast != 1):
            fast = sumOfSq(sumOfSq(fast))
            slow = sumOfSq(slow)
            if fast == slow:
                return False
        return True





'''
To determine cycles we can use two pointers technique, a slow and fast
if they meet at a point until reaching a goal then we have a cycle 
'''