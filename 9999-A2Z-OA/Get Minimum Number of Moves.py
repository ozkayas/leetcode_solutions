'''
Imagine you are shopping on Amazon.com for some good weight lifting equipment. The equipment you want has blocks of many different weights that you can combine to lift.

The listing on Amazon gives you an array, blocks , that consists of n different weighted blocks, in kilograms. There are no two blocks with the same weight. The element blocks[i] denotes the weight of the i th block from the top of the stack. You consider weight lifting equipment to be good if the block at the top is the lightest, and the block at the bottom is the heaviest.

More formally, the equipment with array blocks will be called good weight lifting equipment if it satisfies the following conditions assuming the index of the array starts from 1:

blocks[1] < blocks[i] for all 2 ≤ i ≤ n
blocks[i] < blocks[n] for all 1 ≤ i ≤ n-1
In one move, you can swap the order of adjacent blocks. Find out the minimum number of moves required to form good weight lifting equipment.


Function Description

Complete the function getMinNumMoves in the editor.

getMinNumMoves has the following parameter:

int blocks[n] : the distinct weights

Returns

int : the minimum number of operations required


Example 1 :

Input: blocks = [2, 4, 3, 1, 6]
Output: 3
Explanation: The lightest block needs to move left. The heaviest block is already in the correct position.

In the first move, swap the third and the fourth blocks: blocks = [2, 4, 1, 3, 6].
Swap the second and the third blocks: blocks = [2, 1, 4, 3, 6].
Swap the first and the second blocks: blocks = [1, 2, 4, 3, 6].

Example 2 :

Input: blocks = [4, 11, 9, 10, 12]
Output: 0
Explanation: The blocks are already in their correct positions.


Example 3 :

Input: blocks = [3, 2, 1]
Output: 3
Explanation: Let the blocks be in the order: blocks = [3, 2, 1]

In the first move, we swap the first and the second blocks. After swapping, the order becomes: blocks = [2, 3, 1]

In the second move, we swap the second and the third blocks. After swapping, the order becomes: blocks = [2, 1, 3]

In the third move, we swap the first and second blocks. After swapping, the order becomes: blocks = [1, 2, 3]

Now, the array satisfies the condition after 3 moves.


Constraints:
2 ≤ n ≤ 10^5
1 ≤ blocks[i] ≤ 10^9 for all 1 ≤ i ≤ n
blocks consists of distinct integers.

'''
from typing import List


def getMinNumMoves(blocks:List[int]) -> int:
    #Find indexes of min, max
    minn, maxx = (float('inf'), -1), (float('-inf'), -1)
    for i, n in enumerate(blocks):
        if n < minn[0]:
            minn = (n, i)
        if n > maxx[0]:
            maxx = (n, i)

    print("min, max", minn, maxx)

    # Moves needed to bring min to the beginning
    movesForMin = minn[-1]
    movesForMax = len(blocks)-maxx[-1]-1
    totalMoves = movesForMin + movesForMax

    # If max on the left of the min, it is also swapped a step while moving min, so deduce this step.
    if maxx[-1] < minn[-1]:
        totalMoves -= 1

    return totalMoves

print(getMinNumMoves([2, 4, 3, 1, 6]))
print(getMinNumMoves([4, 11, 9, 10, 12]))
print(getMinNumMoves([3, 2, 1]))