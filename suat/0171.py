class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        digit = 0 
        sum = 0

        for i in range(len(columnTitle)-1,-1,-1):
            c = columnTitle[i]
            sum += self.toNum(c) * 26**digit  
            digit += 1  
        return sum




    def toNum(self, c:str) -> int:
        return ord(c) - ord('A') +1







        '''
        AA -> A * 26 + A
        AZ -> A * 26 + Z = 26 + 26 = 52
        BA -> B * 26 + A = 2*26 + 1 = 53
        ...
        ZZ -> Z * 26 + Z = 26*26 + 26 = 702
        AAA -> A * 26^2 + A * 26 + A = 703
        '''