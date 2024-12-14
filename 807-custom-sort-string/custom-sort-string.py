class Solution:
    def customSortString(self, order: str, s: str) -> str:
        sFreq = defaultdict(int)
        for ch in s:
            sFreq[ch] += 1
        # print(sFreq)

        output = []
        for o in order:
            if o in sFreq:
                for _ in range(sFreq[o]):
                     output.append(o)
                del sFreq[o]

        if len(sFreq) > 0:
            for k,v in sFreq.items():
                for _ in range(v):
                    output.append(k)
            
        return "".join(output)


        