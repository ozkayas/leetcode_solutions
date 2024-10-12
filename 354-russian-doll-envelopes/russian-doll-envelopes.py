class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # This problem is a mixture of weakest character and Longest Incresing Subsequence
        evs = sorted(envelopes, key = lambda x:(x[0], -x[-1]))
        vals = [b for a,b in evs]

        # LIS in vals (reverse sorted)
        # TLE veriyor burasi n2, o yuzden uzerine yazan nlog  LIS metodu kullan
        # i, j = 1, 0
        # dp = [1 for _ in range(len(vals))]

        # while i < len(vals):
        #     while j < i:
        #         if vals[j] < vals[i]:
        #             dp[i] = max(dp[i], dp[j]+1)
            
        #         j += 1
        #     j = 0
        #     i += 1

        # NlogN LIS method:
        ans, temp = 0, []
        for val in vals:
            if not temp:
                temp.append(val)
            else:
                idxForVal = bisect_left(temp, val)
                if idxForVal == len(temp):
                    temp.append(val)
                else:
                    temp[idxForVal] = val
            ans = max(ans, len(temp))

        return ans
        