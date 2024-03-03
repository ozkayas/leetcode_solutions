class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        ans = 0
        prevEnd = intervals[0][1]

        for interval in intervals[1:]:
            if interval[0] < prevEnd:
                # if there is an overlap guard the one with smaller end
                # this is similar to get rid of the other one,
                prevEnd = min(prevEnd, interval[1])
                ans += 1
            else:
                prevEnd = interval[1]
        return ans


        