class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        i = 0
        timer = 0

        while True:
            if tickets[i] > 0:
                tickets[i] -= 1
                timer += 1
                if tickets[i] == 0 and i == k:
                    return timer
            
            i += 1
            i = i%len(tickets)



