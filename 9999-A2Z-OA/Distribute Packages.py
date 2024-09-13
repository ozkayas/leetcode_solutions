"""
Amazon has to distribute multiple packages across all of their delivery trucks. Given an array of trucks where trucks[i] represents the ith truck quantity. We also have another input to_distribute which states the number of packages we want to distribute across all the trucks. So how would we distribute the to_distribute number such that the max total of each truck is minimized?

Function Description

Complete the function distributePackages in the editor.

distributePackages has the following parameters:

1. int[] trucks: an array of integers representing the quantity of each truck
2. int to_distribute: the number of packages to distribute
Returns

int[]: an array representing the distributed packages across the trucks

Example 1:

Input:  trucks = [2, 3, 4, 5, 6], to_distribute = 10
Output: [6, 6, 6, 6, 6]
Explanation:

      This means that 4 packages go to the first truck, 3 packages to the second truck, 2 packages to the third truck, 1 package to the fourth truck, and none to the fifth truck, resulting in each truck having a total of 6 packages.
"""


def solve(trucks, dist):
    maxElement = max(trucks)
    n = len(trucks)

    # Distribute packages to minimize the maximum load among trucks
    for i in range(n):
        if maxElement == trucks[i]:
            continue
        diff = maxElement - trucks[i]
        if dist > diff:
            trucks[i] += diff
            dist -= diff
        else:
            trucks[i] += dist
            dist = 0

        if dist == 0:
            break

    # If there are remaining packages to distribute
    if dist > 0:
        remainder = dist % n
        even = dist // n

        for i in range(n):
            if remainder > 0:
                trucks[i] += (even + 1)
                remainder -= 1
            else:
                trucks[i] += even

            if remainder == 0 and even == 0:
                break

    return trucks


# Example usage
trucks = [2, 3, 4, 5, 6]
to_distribute = 10

res = solve(trucks, to_distribute)
print(res)
