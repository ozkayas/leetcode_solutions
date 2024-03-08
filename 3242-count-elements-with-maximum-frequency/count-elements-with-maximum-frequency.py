class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        mostFreqs = []
        res = 0

        for k,v in freq.items():
            if not mostFreqs:
                mostFreqs.append([k,v])
            else:
                if v > mostFreqs[-1][1]:
                    mostFreqs.clear()
                    mostFreqs.append([k,v])
                elif v == mostFreqs[-1][1]:
                    mostFreqs.append([k,v])

        for item in mostFreqs:
            res += item[1]
        return res
        