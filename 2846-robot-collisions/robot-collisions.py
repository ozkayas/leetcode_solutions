class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # List[tuple] (position, health, direction) 
        robots : List[List] = []

        for i in range(n):
            robots.append([positions[i], healths[i], directions[i], i]) 

        robots.sort(key = lambda item:item[0])
        stack = []


        for robot in robots:
            if not stack or robot[2] == "R" or stack[-1][2] == "L":
                stack.append(robot)
            # last robot is R and cur Robot is L 
            # while last robot is R or robot has healt, collide them
            else: 
                robotHealth = robot[1]
                while stack and stack[-1][2] == "R" and robotHealth > 0:
                    lastInStackHealth = stack[-1][1]
                    if lastInStackHealth > robotHealth:
                        lastInStackHealth -= 1
                        stack[-1][1] = lastInStackHealth
                        break
                    elif lastInStackHealth == robotHealth:
                        stack.pop()
                        robotHealth = 0
                        break
                    else:
                        stack.pop()
                        robotHealth -= 1
                        robot[1] = robotHealth
                if (not stack or stack[-1][2] == "L") and robotHealth > 0 and robot[2] == "L":
                    stack.append(robot)
                        
        
        # print(stack)
        
        stack.sort(key = lambda item:item[-1])
        remainingHealths = [robot[1] for robot in stack]
        return remainingHealths

        