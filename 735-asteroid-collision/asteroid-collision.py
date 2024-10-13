class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for a in asteroids:
            collision_occurred = False
            while res and a < 0 < res[-1]:
                if res[-1] < -a:
                    res.pop()
                elif res[-1] == -a:
                    res.pop()
                    collision_occurred = True
                    break
                else:
                    collision_occurred = True
                    break
            if not collision_occurred:
                res.append(a)
        return res
 