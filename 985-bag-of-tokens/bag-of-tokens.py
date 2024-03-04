class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        if not tokens or tokens[0] > power: return 0
        c, s, e = 0, 0, len(tokens)-1
        res = 0

        while s <= e:
            if tokens[s] <= power:
                power -= tokens[s]
                c += 1
                s += 1
                res = max(res, c)

            elif tokens[e]+power > tokens[s]: # get tokens we can move on the game
                c -= 1
                power += tokens[e]
                e -= 1

            else:
                break
        
        return res

        

'''
          e
[100,200,300,400]
          s       
 
 p = 000
 c = 2
'''