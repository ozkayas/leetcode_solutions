class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        direction = "N"

        def move(inst:str):
            nonlocal direction
            if inst == "G":
                if direction == "N":
                    pos[1] += 1
                elif direction == "S":
                    pos[1] -= 1
                elif direction == "W":
                    pos[0] -= 1
                elif direction == "E":
                    pos[0] += 1                            
            elif inst == "R":
                if direction == "N":
                    direction = "E"
                elif direction == "S":
                    direction = "W"
                elif direction == "W":
                    direction = "N"
                elif direction == "E":
                    direction = "S"
            elif inst == "L":
                if direction == "N":
                    direction = "W"
                elif direction == "S":
                    direction = "E"
                elif direction == "W":
                    direction = "S"
                elif direction == "E":
                    direction = "N"

        for inst in instructions:
            move(inst)

        if pos[0] == 0 and pos[1] == 0 and direction == "N":
            return True
        
        if direction != "N":
            return True

        return False
