class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i:i[0])
        # A min heap will be used to store table keys, so each time we can reach the smallest key
        keys = []
        heapq.heapify(keys)
        # Init heap with the first interval
        rightOfFirst = intervals[0][-1]
        heapq.heappush(keys, rightOfFirst)

        # Gruptaki son elemanin right degeri ile heap icinde tutabiliriz
        for i in range(1, len(intervals)):
            left, right = intervals[i]
            # Can we insert in the first group
            if keys[0] < left:
                heapq.heappop(keys)
            heapq.heappush(keys, right)
        return len(keys)




        