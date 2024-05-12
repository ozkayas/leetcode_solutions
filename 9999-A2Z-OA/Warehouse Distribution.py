'''
Amazon has several warehouses that store piles of boxes containing goods to be shipped.

In one such warehouse, there are a total of n piles numbered 1, 2, ..... n, where the ith pile has boxes[i] number of boxes. To have an even distribution of boxes, the caretaker can do the following operation any number of times (possibly zero):

Choose two distinct piles, i and j(1 <= i, j <= n), such that boxes[i]> 0.
Remove one box from pile i and place it on pile j. More formally, increment boxes[j] by 1 and decrement boxes[i] by 1.
For even distribution, the caretaker wishes to minimize the difference between the maximum and the minimum number of boxes in the piles. Call the minimum difference achievable d. The goal is to find the minimum number of operations required to achieve the difference d.

Function Description

Complete the function findMinimumOperations in the editor.

findMinimumOperations has the following parameter:

int boxes[n]: the number of boxes in each pile
Returns

long_int: the min number of operations to achieve the min possible difference
❀⊱ Credit to eva 🌷 ⊰❀

Example 1:

Input:  boxes = [5, 5, 8, 7]
Output: 2 
Explanation:
Consider the number of piles to be n = 4 and the boxes in them are boxes = [5, 5, 8, 7]. The minimum possible difference that can be achieved is 1 by transforming the piles into [6, 6, 7, 6] as below. Hence the answer is 2.
      
      
Example 2:

Input:  boxes = [2, 4, 1]
Output: 1 
Explanation:

Move a box from pile 2 to pile 3: [2, 4, 1] -> [2, 3, 2]
      
Example 3:

Input:  boxes = [4, 4, 4, 4, 4]
Output: 0 
'''

def findMinimumOperations(boxes) -> int:
    total = sum(boxes)
    average = total//len(boxes)

    moves = 0

    for h in boxes:
        if h < average:
            moves += (average - h)
    
    return moves


print(findMinimumOperations([5, 5, 8, 7]))
print(findMinimumOperations([2, 4, 1]))
print(findMinimumOperations([4, 4, 4, 4, 4]))