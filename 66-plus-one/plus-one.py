class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        remainder = 1
        ans = []
        for n in reversed(digits):
            curTot = n+remainder
            ans.append(curTot%10)
            remainder = curTot//10
        
        if remainder:
            ans.append(1)
        
        return ans[::-1]
        