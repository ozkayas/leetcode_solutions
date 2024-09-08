class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        freq = []
        if a > 0: freq.append([a,"a"])
        if b > 0: freq.append([b,"b"])
        if c > 0: freq.append([c,"c"])
        
        ans = []
        while freq:
            freq.sort(key = lambda item:-item[0])
            cur = freq[0][1]
            if len(ans) < 2 or ans[-2:] != [cur, cur]:
                ans.append(cur)
                freq[0][0] -= 1
                if freq[0][0] == 0: freq.pop(0)
            # we will try to use next if exists, otherwise stop loop
            elif len(freq) == 1:
                break
            else:
                nxt = freq[1][1]
                ans.append(nxt)
                freq[1][0] -= 1
                if freq[1][0] == 0: freq.pop(1)

        return "".join(ans)
        








"""
a2 b1 c9

cc a cc a cc b cc

"""