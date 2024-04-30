'''
https://www.fastprep.io/problems/amazon-make-power-non-decreasing
AWS provides scalable system. A set of n servers are used for horizontally scaling an application.

The goal is to have the computational power of the servers in non-decreasing order. 
To do so, you can increase the computational power of each server in any contiguous segment by x. 
Choose the values of x such that after the computational powers are in non-decreasing order , the sum of the x values is minimum.
Example 1:
                     
Input:  power = [3, 4, 1, 6, 2]
                       ^
                       3
Output: 7 
Explanation:
Add 3 units to the subarray [2, 4] and 4 units to the subarray [4, 4,]. 
The final arrangement of the server is: [3, 4, 4, 9, 9]. 
The ans is 3 + 4 = 7. (As shown in the image)
Example 2:

Input:  power = [3, 2, 1]
Output: 2 
Explanation:
Add 1 unit to subarray (1, 2) and 1 unit to subarray (2, 2). The final arrangement of server is [3, 3, 3]

'''
from typing import List

def makePowerNonDecreasing(power:List[int]) -> int:
    if len(power) < 2 : return 0

    toAdd = 0

    for i in range(1,len(power)):
        if power[i] + toAdd < power[i-1]:
            toAdd += power[i-1] - (power[i] + toAdd) # toAdd = 7
            power[i] += toAdd
        else:
            power[i] += toAdd

    return toAdd


print(makePowerNonDecreasing([3, 4, 1, 6, 2]))
print(makePowerNonDecreasing([3, 2, 1]))