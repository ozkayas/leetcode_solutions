class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        freq = defaultdict(int)
        most = 0
        mostCh = None
        for c in s:
            freq[c] += 1
            if freq[c] >= most:
                most = freq[c]
                mostCh = c

        # aaab - NOK 4//2:2
        # aaabb - OK 5//2:2  , aaaab - NOK
        # aaaabb - NOK 6//2:3
        if most * 2 - 1 > len(s): return ""

        ### Sort ederek daha kisa bir kod yazilabilir, freq sort edilerek

        output = ["" for _ in range(N)]
        i = 0
        # Fill most common char firstly
        for _ in range(most):
            output[i] = mostCh
            i = i+2 if i+2<N else 1
        # remove mostCh from table
        del freq[mostCh]
        # Insert remainings
        for ch, f in freq.items():
            for _ in range(f):
                output[i] = ch
                i = i+2 if i+2<N else 1

        return "".join(output)




        




        