class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        f, s = 0, 0 # poiinters for first and second lists
        ans = []

        def intersect(f_interval: List[int], s_interval: List[int]) -> List[int] | None:
            # Start is the max of both starts, end is the min of both ends
            start = max(f_interval[0], s_interval[0])
            end = min(f_interval[1], s_interval[1])
            if start <= end:  # Valid intersection
                return [start, end]
            return None

        # Shift pointer of the pair whose end time is smaller
        def updatePointers():
            nonlocal f,s
            if firstList[f][-1] < secondList[s][-1]:
                f += 1
            elif firstList[f][-1] > secondList[s][-1]:
                s += 1
            else:
                f += 1
                s += 1


        while f < len(firstList) and s < len(secondList):
            first = firstList[f]
            second = secondList[s]

            intersection = intersect(first, second)
            # print(intersection)
            if intersection: 
                ans.append(intersection)

            updatePointers()

        return ans
        