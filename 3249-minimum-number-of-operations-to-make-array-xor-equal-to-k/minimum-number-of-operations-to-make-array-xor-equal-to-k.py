class Solution:
    def minOperations(self, v: List[int], k: int) -> int:

        ### I did not get it well.
        ## Just watched and copied the code this time.
        
        n = len(v)
        ans = 0
        for i in range(31):
            b = 0
            for j in range(n):
                if ((v[j] >> i) & 1) == 1:
                    b = b ^ 1
            if ((k >> i) & 1) != b:
                ans += 1
        return ans
