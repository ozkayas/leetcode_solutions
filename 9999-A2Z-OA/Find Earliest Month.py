'''
https://www.fastprep.io/problems/amazon-find-earliest-month

The interns at Amazon were asked to review the company's stock value over a period. Given the stock prices of n months, the net price change for the ith month is defined as the absolute difference between the average of stock prices for the first i months and for the remaining (n - i) months where 1 ≤ i < n. Note that these averages are rounded down to an integer.
Given an array of stock prices, find the month at which the net price change is minimum. If there are several such months, return the earliest month.
Note: The average of a set of integers here is defined as the sum of integers divided by the number of integers, rounded down to the nearest integer. For example, the average of [1, 2, 3, 4] is the floor of (1 + 2 + 3 + 4) / 4 = 2.5 and the floor of 2.5 is 2.

Function Description
Complete the function findEarliestMonth in the editor.
findEarliestMonth has the following parameter:

int[] stockPrice: an array of integers representing the stock prices
Returns
int: the earliest month at which the net price change is minimum

Example 1:
Input:  stockPrice = [1, 3, 2, 3]
Output: 2 
Explanation:
The minimum net price change is 0, and it occurs in the 2nd month. Return 2 :)
      
Example 2:
Input:  stockPrice = [1, 3, 2, 4, 5]
Output: 2 
Explanation:

The net price change can be calculated as:

      
Month 1: [1] and [3, 2, 4, 5], their respective averages, rounded down = 1 and 3, net price change = 2


Month 2: [1, 3] and [2, 4, 5], averages = 2 and 3, net price change = 1


Month 3: [1, 3, 2] and [4, 5], averages = 2 and 4, net price change = 2


Month 4: [1, 3, 2, 4] and [5], averages = 2 and 5, net price change = 3

The minimum net price change is 1, and it occurs at month 2 :D.

'''

