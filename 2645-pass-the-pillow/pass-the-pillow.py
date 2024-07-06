class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        tick = 0
        pillowHolder = 1
        isGoingRight = True

        while tick < time:
            tick += 1

            if isGoingRight:
                pillowHolder += 1
            else:
                pillowHolder -= 1
            
            if pillowHolder == n:
                isGoingRight = False
            if pillowHolder == 1:
                isGoingRight = True
                
        return pillowHolder



        



            


        