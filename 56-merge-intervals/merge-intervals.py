class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []

        intervals.sort(key=lambda x:x[0])
        for interval in intervals:
            if not ans:
                ans.append(interval)
            else:
                if interval[0] <= ans[-1][-1]:
                    ans[-1][-1] = max(interval[-1], ans[-1][-1])
                else:
                    ans.append(interval)
            
        return ans

