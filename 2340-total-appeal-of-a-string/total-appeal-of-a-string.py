class Solution:
    ### Contribution Method !!!
    ### Explanation https://www.youtube.com/watch?v=18Agi7XCGAI

    def appealSum(self, s: str) -> int:
        N = len(s)
        lastSeenIndex = dict()
        ans = 0

        for i,ch in enumerate(s):
            left, right = 1, N-i
            if ch in lastSeenIndex:
                left = i - lastSeenIndex[ch]
            else:
                left = i+1
            
            ans += left*right
            lastSeenIndex[ch] = i

        return ans