class Solution:

    def __init__(self, w: List[int]):
        self.probabilities = []
        total = sum(w)
        pfSum = 0
        for i in range(len(w)):
            pfSum += w[i]
            self.probabilities.append(pfSum/total)

    def pickIndex(self) -> int:
        # print(self.probabilities)
        rand = random.uniform(0,1)
        return bisect_left(self.probabilities, rand)
        
"""
[1,2,7]
sum = 10
i: value, probabilty(val/sum)
0: 0.10 (1/10)
1: 0.20 (2/10)
2: 0.70 (7/10)
cumulatives needed
[0.1, .30, 1]

random.uniform(0,1)
search for this in probabiliy list using binary search bisect_left may work
"""


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()