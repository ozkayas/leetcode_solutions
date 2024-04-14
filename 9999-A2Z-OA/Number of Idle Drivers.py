'''
https://www.fastprep.io/problems/amazon-num-idle-drives
Amazon uses small, Roomba-shaped robots, called "Drives". They deliver large stacks of products to human workers by following set paths around the warehouse.

The warehouse can be represented in the form of a cartesian plane, where robots are located at integral points of the form (x, y). When a product is to be delivered to some point (i, j), the nearest robot is sought and chosen. Thus if a robot is surrounded by other robots nearby, it will seldom be chosen for work. More formally, a robot is said to be idle if it has a robot located above, below, left, and right of it. It is guaranteed that no two robots are at the same location.

Given the locations of n robots, find the number of idle robots.

Function Description

Complete the function numIdleDrives in the editor below.

numIdleDrives has the following parameters:

int x[n]: x[i] is the x-coordinate of the ith robot, where 0 ≤ i < n.
int y[n]: y[i] is the y-coordinate of the ith robot, where 0 ≤ i < n.
Returns

int: the number of idle robots

Example 1:

Input:  x = [0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1], y = [-1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0]
Output: 5 
Input:  x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3], y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]
Output: 2 
'''
## INPUTS
x = [0, 0, 0, 0, 0, 1, 1, 1, 2, -1, -1, -2, -1]
y = [-1, 0, 1, 2, -2, 0, 1, -1, 0, 1, -1, 0, 0]

# x = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
# y = [1, 2, 3, 1, 2, 3, 5, 1, 2, 3]

## First Create vertical and horizontal limits for each axis point
vertical_limits, horizontal_limits = dict(), dict()  # 1: [-2,2]

# Fill vertical Limits for each X position
for i in range(len(x)):
    if x[i] not in vertical_limits:
        vertical_limits[x[i]] = [y[i],y[i]]
    else:
        vertical_limits[x[i]][0] = min(vertical_limits[x[i]][0], y[i])
        vertical_limits[x[i]][1] = max(vertical_limits[x[i]][1], y[i])

# Fill horizontal Limits for each X position
for i in range(len(x)):
    if y[i] not in horizontal_limits:
        horizontal_limits[y[i]] = [x[i],x[i]]
    else:
        horizontal_limits[y[i]][0] = min(horizontal_limits[y[i]][0], x[i])
        horizontal_limits[y[i]][1] = max(horizontal_limits[y[i]][1], x[i])

def is_idle_vertically(x:int, y:int) -> bool:
    return vertical_limits[x][0] < y < vertical_limits[x][1]


def is_idle_horizontally(x:int, y:int) -> bool:
    return horizontal_limits[y][0] < x < horizontal_limits[y][1]
    
## MAIN LOOP
counter = 0 

for i in range(len(x)):
    if is_idle_vertically(x[i],y[i]) and is_idle_horizontally(x[i],y[i]):
        counter += 1

print("RESULT: ", counter)