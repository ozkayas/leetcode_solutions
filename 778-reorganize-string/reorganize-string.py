class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = list(Counter(s).items())
        freq.sort(key = lambda i:i[1], reverse = True)
        # print(freq)

        #fast exit if most common can not be filled in the space
        most = freq[0][1]
        if most * 2 - 1 > len(s): return ""

        ans = ["" for _ in range(len(s))]
        i = 0 # global pointer first fill 0 2 4 6 ,then reset to 1 an fill 1 3 5 7 etc.
        for ch, f in freq:
            for _ in range(f):
                # print(i, ch)
                ans[i] = ch
                i = i+2 if i+2 < len(s) else 1
        
        return "".join(ans)


        
        