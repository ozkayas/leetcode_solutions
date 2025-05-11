class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y,dx,dy = 0,0,0,1

        for ins in instructions:
            if ins == "G":
                x += dx
                y += dy
            else:
                if ins == "L": # 0,1 -> -1,0
                    dx, dy = -dy, dx
                else: # 0,1 -> 1,0 -> 0,-1, -1,0
                    dx, dy = dy, -dx

        if x == y == 0:
            return True
        elif (dx,dy) != (0,1):
            return True
        return False

        