class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        N = len(hand)
        if N % groupSize != 0: return False
        hand.sort()
        flag = [1 for _ in range(N)]

        s = 0

        while s < N:
            while s < N and flag[s] == 0:
                s += 1

            # bir baslangic noktasi bulduk [1,2,3] 1 bulduk
            e = s            
            if s == N:
                break

            subarr = []
            for i in range(groupSize):
                if e >= N: return False
                if subarr and subarr[-1]+1 != hand[e]:
                    return False
                subarr.append(hand[e])
                flag[e] = 0
                while e < N and (flag[e] == 0 or hand[e] == subarr[-1]):
                    e += 1
            print(subarr)
            if len(subarr) < groupSize:
                return False

        return True


            
        




"""

1 1 1 2 2 2 3 3 3
f t t f f t f t t

  s.          e 
   




""" 

        