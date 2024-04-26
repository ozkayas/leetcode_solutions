'''
In an Amazon coding marathon, the following challenge was given.


## LEETCODE SIMILAR

===>> https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

The uniqueness of an array of integers is defined as the number of distinct elements present. 
For example, the uniqueness of [1, 5, 2, 1, 3, 5] is 4, element values 1, 2, 3, and 5. 
For an array arr of n integers, the uniqueness values of its subarrays is generated and stored in another array, call it subarray_uniqueness for discussion. 
Find the median of the generated array subarray_uniqueness.

Notes:
The median of a list is defined as the middle value of the list when it is sorted in non-decreasing order. 
If there are multiple choices for median, the smaller of the two values is taken. For example, the median of [1, 5, 8] is 5, and of [2, 3, 7, 11] is 3.
A subarray is a contiguous part of the array. For example, [1, 2, 3] is a subarray of [6, 1, 2, 3, 5] but [6, 2] is not.
Function Description

Complete the function findMedianOfSubarrayUniqueness in the editor.

findMedianOfSubarrayUniqueness has the following parameter:
int arr[n]: the array
Returns
int: the median of the generated array subarray_uniqueness

Constraints
1 ≤ n ≤ 10^5
1 ≤ arr[i] ≤ n

Input:  arr = [1, 1]
Output: 1 
Explanation:

The subarrays along with their uniqueness values are:
        
[1]: uniqueness = 1
[1, 1]: uniqueness = 1
[1]: uniqueness = 1

subarray_uniqueness is [1, 1, 1].

      
Example 2:

Input:  arr = [1, 2, 3]
Output: 1 
Explanation:

Given n = 3 and arr = [1, 2, 3], the subarrays along with their uniqueness values are:
[1]: uniqueness = 1
[1, 2]: uniqueness = 2
[1, 2, 3]: uniqueness = 3
[2]: uniqueness = 1
[2, 3]: uniqueness = 2
[3]: uniqueness = 1
  subarray_uniqueness is [1, 2, 3, 1, 2, 1], and after sorting it is [1, 1, 1, 2, 2, 3].
     
      
Example 3:
Input:  arr = [1, 2, 1]
Output: 1 
Explanation:
The subarrays with their uniqueness values are:

[1]: uniqueness = 1
[1, 2]: uniqueness = 2
[1, 2, 1]: uniqueness = 2
[2]: uniqueness = 1
[2, 1]: uniqueness = 2
[1]: uniqueness = 1

The subarray_uniqueness array is [1, 2, 2, 1, 2, 1]. After sorting, the arr is [1, 1, 1, 2, 2, 2]. 
The choice is between the two bold values. Return the min of the two, 1.
[1]: uniqueness = 1

'''

'''
           
'''
from typing import List
array = [1, 2, 3]
# arr = [1, 2, 1]

def medianForPair(a:int, b:int, subarr:List[int]) -> int:
    return subarr[(a+b)//2]
    

def findMedianOfSubarrayUniqueness(arr:List[int]) -> int:


print(findMedianOfSubarrayUniqueness(array))