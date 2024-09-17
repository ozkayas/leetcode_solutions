class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        st = []

        intervals.sort()
        for s,e in intervals:
            if not st or s > st[-1][1]:
                st.append([s,e])
            else:
                st[-1][1] = max(st[-1][1], e)


        return st
        