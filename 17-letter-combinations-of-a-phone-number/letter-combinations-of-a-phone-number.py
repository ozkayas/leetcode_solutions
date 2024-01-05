class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        # character map
        cMap  = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        # last index to decide for reaching base case
        maxIndex = len(digits)-1
        result = []

        def fn(i:int, arr:str):
            # print("fn called -> i:{}, arr:{}".format(i, arr))
            num = digits[i]

            for s in cMap[num]:
                arrCopy = arr+s
                if i == maxIndex:
                    result.append(arrCopy)
                else:
                    fn(i+1, arrCopy)

            return    

        fn(0, "")
        return result

        