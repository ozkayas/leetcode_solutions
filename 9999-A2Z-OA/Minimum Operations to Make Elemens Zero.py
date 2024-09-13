"""
########################################################################################################
########## QUESTION: 3
########################################################################################################

In this problem, you are given an integer array and you need to perform some operations on the array to make all the elements equal to 0. In one operation, you can select a prefix of the given array and increment or decrement all the elements of the prefix by 1.

You have an array, arr, consisting of n integers. Find the minimum number of operations required to convert every element of this array to 0.

A prefix is a contiguous group of items that includes the first element in the cart. For example, [1], [1, 2], [1, 2, 3] etc are prefixes of [1, 2, 3, 4, 5].

Note: It is guaranteed that it is always possible to convert every element of the array to 0.

Example:

arr = [3, 2, 1]

The most efficient approach is:

Operation 1: Let the prefix length be 2, and decrement by 1. cart after this operation is [2, 1. 1]

Operation 2: Let the prefix length be 1, and decrement by 1. cart after this operation is [1, 1, 1].

Operation 3: Let the prefix length be 3. and decrement by 1. cart after this operation is [0. 0. 0].

The answer is 3. Note that it is not possible make all the elements of the array 0 in fewer operations.

Function Description

Complete the function getMinimumOperations in the editor below.

getMinimumOperations has the following parameter:
arr[n]: an array of integers

Returns:

int: denoting the minimum number of operations required to convert every element to 0

arr = [3, 2, 0, 0, -1]

For n=5 and cart - [3, 2, 0, 0, -1], one optimal set of operations is:

Operation 1: Let the prefix length be 1, and decrement by 1. cart after this operation is [2,2,0,0,-1]

Operation 2: Let the prefix length be 2, and decrement by 1. carr after this operationvis [1,1,0,0,-1]

Operation 3: Let the prefix length be 4, and decrement by 1. cart after this operation is [0,0,0,0,-1]
Operation 4: Let the prefix length be 2, and decrement by 1. cart after this operation is [-1,-1,-1,-1,-1]

Operation 5: Let the prefix length be 5, and increment by 1. cart after this operation is [0,0,0,0,0]

The answer is 5.
"""

def minOperations(arr) -> int:
    cur = arr[0]
    operations = 0

    for i in range(1, len(arr)):
        target = arr[i]
        operations += abs(cur - target)
        cur = target

    operations += abs(cur - 0)

    print(operations)
    return operations

from Scripts.test_utils import test_case
test_case(minOperations,([3, 2, 1],),3)
test_case(minOperations,([3, 2, 0, 0, -1],),5)
test_case(minOperations,([0, 0, 1, 2],),4)
