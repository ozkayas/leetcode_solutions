'''
Group Students (AS Intern, it may apply to other interns) 🍑
🤘 INTERN
Amazon Technical Academy (ATA) provides in-demand, technical training to current Amazon employees looking to broaden their skill sets. ATA has admitted a group of n prospective trainees with varying skill levels. To better accommodate the trainees, ATA has decided to create classes tailored to the skill levels. A placement examination will return a skill level that will be used to group the trainees into classes, where levels[i] represents the skill level of trainee i. All trainees within a class must have a skill level within maxSpread, a specified range of one another. Determine the minimum number of classes that must be formed.

Function Description

Complete the function groupStudents in the editor.

groupStudents has the following parameter(s):

int levels[n]: the skill level for each student
int maxSpread: the maximum allowed skill level difference between any two members of a class
Returns

int: the minimum number of classes that can be formed

Example 1:

Input:  levels = [1, 4, 7, 3, 4], maxSpread = 2
Output: 3 
Explanation:

The trainees in any class must be within maxSpread = 2 levels of each other. In this case, one optimal grouping is (1, 3), (4, 4), and (7). Another possible grouping is (1), (3, 4, 4), (7). There is no way to form fewer than 3 classes.
'''

from typing import List
def groupStudents(levels:List[int], maxSpread:int) -> int:
    levels.sort()
    groupCounter = 0

    l, r = 0, 0

    while r < len(levels):
        while r < len(levels) and  levels[r] - levels[l] <= maxSpread:
            r += 1
        
        groupCounter += 1
        l = r
    
    # After the loop if l is still inside the levels, we may add one last group
    if l < len(levels):
        groupCounter += 1
    
    return groupCounter

print(groupStudents([1,4,7,3,4], 2))
print(groupStudents([], 2))                 # Output: 0 (Empty array)
print(groupStudents([5], 2))                # Output: 1 (Single trainee)
print(groupStudents([3, 3, 3, 3], 0))        # Output: 1 (Uniform skill levels, spread = 0)
print(groupStudents([1, 4, 7, 10], 5))       # Output: 2 (Large spread within bounds)
print(groupStudents([2, 5, 1, 8, 3, 6], 3))   # Output: 3 (Uneven distribution with overlap)

