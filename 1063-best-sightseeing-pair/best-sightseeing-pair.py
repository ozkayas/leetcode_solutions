class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        spot = values[0] #max spot val[i]+i so far

        for i in range(1, len(values)):
            res = max(res, spot + values[i]-i)
            spot = max(spot, (values[i]+i))

        return res