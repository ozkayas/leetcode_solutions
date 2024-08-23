class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # edge case
        if len(hand) % groupSize != 0:
            return False
        numOfGroups = int(len(hand) // groupSize)
        
        freq = defaultdict(int)


        for card in hand:
            freq[card] += 1

        def getMin(freq: dict) -> int:
            # print(freq.keys())
            return min(freq.keys())

        def canGroupN(freq: dict) -> bool:
            cur = getMin(freq)
            for i in range(groupSize):
                if freq[cur] > 0:
                    freq[cur] -= 1
                    if freq[cur] == 0:
                        del freq[cur]
                    cur += 1
                else:
                    return False
            return True

        while numOfGroups:
            if canGroupN(freq):
                numOfGroups -= 1
                continue
            else:
                return False
            

        return True