from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        pairs = 0

        hMap = defaultdict(int) # Will hold frequencies of nums % 60

        for t in time:
            cur = t % 60
            pair_of_cur = 0 if cur == 0 else 60 - cur

            # Look for a pair already found
            if pair_of_cur in hMap:
                pairs += hMap[pair_of_cur]

            # Update 
            hMap[cur] += 1
                
        return pairs




'''       time = [30,20,150,100,40] 
                             ^       
       time = [60,60,60] 
                     ^

    map: (num:index) ans = 1+2
        0: 2
        '''