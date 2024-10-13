class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for curr in asteroids:
            curr_survived = True
            # Collusion case, cur moving left and topof the stack to right
            # if astreoid survives it continue crashing to elements on the stack !!!
            while res and curr < 0 < res[-1]:
                if res[-1] < -curr:
                    res.pop() #explode last one
                elif res[-1] == -curr:
                    res.pop()
                    curr_survived = False
                    break # We did not survive, so break the while loop
                else:
                    curr_survived = False
                    break # We did not survive, so break the while loop
            if curr_survived:
                res.append(curr)
        return res
 