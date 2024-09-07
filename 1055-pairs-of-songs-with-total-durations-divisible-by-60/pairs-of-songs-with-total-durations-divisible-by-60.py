class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        secMap = defaultdict(int)
        count = 0

        for t in time:
            t = t%60
            pairOfThis = (60-t)%60
            count += secMap[pairOfThis]
            secMap[t] += 1
        
        return count
        

        
