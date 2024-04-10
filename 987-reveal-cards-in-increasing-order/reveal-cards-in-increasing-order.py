from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res = deque()
        sorted_deck = sorted(deck)

        while sorted_deck:
            res.rotate(-1)
            curr = sorted_deck.pop()
            res.append(curr)

        print(res)
        return reversed(res)

        
'''

[2, 13, 3, 11, 5, 17, 7]
 1.     1.     1.     1


[, , , , , ,    


7 17 5 11 3 13 2

'''