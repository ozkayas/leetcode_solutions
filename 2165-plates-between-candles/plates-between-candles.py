from bisect import bisect_left

class Solution:
    def fillPlateIntervals(self, s:str) -> List[int]:
        intervals = []
        lastBucket = []
        prefixSum = 0
        for i in range(len(s)):
            
            if s[i] == "|":
                lastBucket.append(i)

            # Closing an interval for plates
            if len(lastBucket) == 2:
                # If there is some plate between candles
                platesBetweenCandles = lastBucket[1] - lastBucket[0] -1
                if platesBetweenCandles > 0:
                    prefixSum += platesBetweenCandles
                    intervals.append(lastBucket[:]+[prefixSum])
                lastBucket.clear()
                lastBucket.append(i)

        return intervals


    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:

        totalPlates = []

        intervals = self.fillPlateIntervals(s)
        for q in queries:
            plates = 0
            
            # intervals is sorted so we need to do binary search to find 
            # the first interval[0] bigger >= to q[0]
            # the last interval[1] smaller <= to q[1]
            # which intervals are between the query
            first = bisect_left(intervals, q[0], key=lambda i:i[0])
            last = bisect_left(intervals, q[1]+1, key=lambda i:i[1])-1
            if last >= first:
                lastBucketPlates =  intervals[last][2]
                firstBucketPlates = intervals[first-1][2] if first>0 else 0
                plates = lastBucketPlates - firstBucketPlates

                totalPlates.append(plates)
            else:
                totalPlates.append(0)
    
        return totalPlates




        
'''
* * | * * | * * * |
0 0   2 2   5 5 5
      5 5   9 9 9


* * * | * * | * * * * * | * * |   | * * | *
        3 - 6   6 - 12    12-14   15-18


 3,6 : 2
 6,12: 5
 12,14:2
 15,18:2       

[[1,17], => 9
[4,5], => 0
[14,17], -> 0
[5,11], ->0
[15,16]] ->0


'''