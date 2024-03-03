class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        ans = []

        for i, interval in enumerate(intervals):
            #if no intersection and before new -> just append to result
            if interval[1] < newInterval[0]:
                ans.append(interval)
            #if no intersection and after new -> append new and append the rest
            elif interval[0] > newInterval[1]:
                ans.append(newInterval)
                ans += intervals[i:]
                return ans
            # there is an intersection so just merge interval to newInterval
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])

        ans.append(newInterval)
        return ans