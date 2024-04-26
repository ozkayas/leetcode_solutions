class Solution:

    # BS to first end >= target value, return the index of it
    def getIndexOfMinStart(self, starts:List[int], target) -> int:
        idx = -1
        l, r = 0, len(starts)-1

        while l <= r:
            m = l + (r-l)//2

            if target <= starts[m][0]:
                # We're OK, and try to find a better value on left portion
                idx = starts[m][-1]  # Save the index of this end value for now
                r = m - 1
            else:
                l = m + 1
        return idx



    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ## Fill an array with end times and indexes
        starts = [(intervals[i][0],i)  for i in range(len(intervals))]
        starts.sort() # we need to sort, because we will BS

        output = []
        for interval in intervals:
            output.append(self.getIndexOfMinStart(starts,interval[-1]))

        return output