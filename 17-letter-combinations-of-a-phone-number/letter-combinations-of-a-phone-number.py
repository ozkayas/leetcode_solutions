class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return ""

        cMap = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # print( list(cMap[digits[0]]) )
        
        def rec(digit)-> List[str]:
            
            if digit == len(digits)-1:
                return list(cMap[digits[digit]])
            
            res = []
            nxtNodeRes = rec(digit+1)
            for c in cMap[digits[digit]]:
                for cc in nxtNodeRes:
                    # print(c+cc)
                    res.append(c+cc)
                    # print(res)
            
            return res


        return rec(0)




        
