class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])

        # Init with the first interval
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            nextStart, nextEnd = intervals[i]
            lastEnd = output[-1][-1]
            if nextStart <= lastEnd:
                output[-1][-1] = max(nextEnd, lastEnd)
            else:
                output.append(intervals[i])

        return output

        