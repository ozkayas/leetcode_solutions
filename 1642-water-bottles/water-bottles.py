class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:

        # drink & exchange operation in each loop
        drink = 0
        emptyBottles = 0
        fullBottles = numBottles
        while numBottles >= numExchange:
            drink += fullBottles
            emptyBottles += fullBottles
            # exchange
            fullBottles = emptyBottles // numExchange
            emptyBottles %= numExchange
            numBottles = fullBottles + emptyBottles
            
        # We can not exchange but may have a few fullBottles to drink  
        drink += fullBottles

        return drink
            


        