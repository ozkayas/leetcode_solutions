"""
Find Maximum Zeroes
In an Amazon analytics team, the Analysts collectively have a preference for the number zero and a disapproval towards negative numbers. Their objective is to determine the maximum number of zeroes achievable after performing a series of operations (possibly zero) on an array, all while avoiding negative values.

Formally, given an array arr of size n of positive integers, the Analysts can perform the following operation any number of times (possibly zero):
Choose a prefix of size s (1 ≤ s ≤ n) that doesn't contain any zero (there is no index i such that arr[i] = 0 and 1 ≤ i ≤ s).
Decrease all values of this prefix by one, i.e., set arr[i] = arr[i] - 1 for all 1 ≤ i ≤ s.
Find the maximum number of zeroes that the array arr can contain after performing any (possibly zero) number of operations on the array.
Note that a prefix of size s in an array arr is the first s elements in this array, for example, the prefix of size 3 of array [3, 1, 5, 5, 2] is [3, 1, 5].

Function Description
Complete the function findMaximumZeroes in the editor.
findMaximumZeroes has the following parameters:

int arr[n]: the elements of the array.
Returns

int: the maximum number of zeroes that the array arr can contain after performing any (possibly zero) number of operations on the array.
Example 1:
Input:  arr = [4, 3, 5, 5, 3]
Output: 3
Explanation:
If we perform the following operations:
No further operations can be done on the array, and the number of zeroes in arr is 3, which is the maximum possible.

Constraints:
1 ≤ n ≤ 2 * 105
1 ≤ arr[i] ≤ 109
"""

def findMaximumZeroes(arr) -> int:
    # we need a monotonic non increasing stack starting from the start
    stack = []

    for n in arr:
        if not stack:
            stack.append(n)
        else:
            if n <= stack[-1]:
                stack.append(n)

    return len(stack)


print(findMaximumZeroes([4, 3, 5, 5, 3]))
print(findMaximumZeroes([4, 3, 6, 2, 0, 5, 5, 0]))

