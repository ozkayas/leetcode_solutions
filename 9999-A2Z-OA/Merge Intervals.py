'''
https://www.fastprep.io/problems/amazon-merge-intervals
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]] 
Explanation:
Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
 
Example 2:
Input:  intervals = [[1,4],[4,5]]
Output: [[1,5]] 
Explanation:
Intervals [1,4] and [4,5] are considered overlapping.
           
Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
'''
from typing import List

def mergeIntervals(intervals:List[int]) -> List[int]:
    output = []

    intervals.sort(key = lambda item:item[0])
    output.append(intervals[0])

    for i in range(1, len(intervals)):
        if intervals[i][0] <= output[-1][1]:
            output[-1][1] = intervals[i][1]
        else:
            output.append(intervals[i])

    return output


print(mergeIntervals([[1,3],[2,6],[15,18],[8,10]]))
print(mergeIntervals([[1,4],[4,5]]))
print(mergeIntervals([[1,4],[4,5],[7,8]]))