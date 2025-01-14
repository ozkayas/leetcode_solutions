class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seta = set()
        setb = set()
        res = []

        for i in range(len(A)):
            seta.add(A[i])
            setb.add(B[i])

            res.append(len(seta.intersection(setb)))
        
        return res