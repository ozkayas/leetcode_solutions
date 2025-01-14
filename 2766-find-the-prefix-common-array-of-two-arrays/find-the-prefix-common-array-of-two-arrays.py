class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        # bool array to mark seen
        arr_a = [False for _ in range(N+1)]
        arr_b = [False for _ in range(N+1)]
        res = []
        lastStepCommon = 0

        for i in range(N):
            a, b = A[i], B[i]
            arr_a[a] = True
            arr_b[b] = True
            if a == b:
                lastStepCommon += 1
            else:
                if arr_a[a] and arr_b[a]:
                    lastStepCommon +=1
                if arr_a[b] and arr_b[b]:
                    lastStepCommon +=1

            res.append(lastStepCommon)
        
        return res


        # seta = set()
        # setb = set()
        # res = []

        # for i in range(len(A)):
        #     seta.add(A[i])
        #     setb.add(B[i])

        #     res.append(len(seta.intersection(setb)))
        
        # return res