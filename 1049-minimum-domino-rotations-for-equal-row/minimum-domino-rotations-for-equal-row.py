class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        N = len(tops)
        ans = 0

        # find the common number to reach, 2 in the example
        commonSet = {bottoms[0], tops[0]}

        for i in range(1, N):
            commonSet = commonSet.intersection({bottoms[i],tops[i]})

        print(commonSet)
        if not commonSet: return -1
        commonN = list(commonSet)[0]

        # count #of common num in tops and bottoms
        commonInTop = sum(1 for n in tops if n == commonN)
        commonInBot = sum(1 for n in bottoms if n == commonN)

        if commonInTop > commonInBot:
            return N - commonInTop
        else:
            return N - commonInBot



        