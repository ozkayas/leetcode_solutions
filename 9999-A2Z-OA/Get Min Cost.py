'''
There are n books ordered sequentially numbered 1, 2,.., n, where the ith book has a cost of cost[i]. A customer wants to purchase all the books, and kindle offers the customer a unique scheme is described as the follows -

Let the leftmost book remaining in the sequence be book i. The customer can choose to buy the leftmost book individually for cost[i]. This book is then removed from the sequence.
Let the rightmost book remaining in the sequence be book j. The customer can choose to buy the rightmost book individually for cost[j]. This book is then removed from the sequence.
The customer can also choose to pay the amount pariCost for both the leftmost and rightmost books together. In this case, both the leftmost and rightMostbooks are removed. This option can be used as many as k times.
Given the cost of books cost, the cost to purchase the leftmost and rightmost books together, parCost, and the mx num of times the pairCost option can be applied k, find the min cost in which the customer can purchase all the books following the scheme above.

Function Description

Complete the function getMinCost in the editor.

getMinCost has the following parameters:

int cost[n]: the cost of each book
int pairCost: the cost of purchase the leftmost and rightmost book together
int k: the MAX NUM of times pairCost can be used
Returns

long int: the min cost to purchase all books

Endless thanks to our best friend for their kind help in sharing the source!

Example 1:

Input: cost = [1, 2, 3], pairCost = 2, k = 1
Output: 3

Example 2:

Input: cost = [1, 1, 1], pairCost = 2, k = 1
Output: 3
Explanation:

Purchase the books individually for 1 + 1 + 1 = 3.

Example 3:

Input: cost = [9, 11, 13, 15, 17], pairCost = 6, k = 2
Output: 21
Explanation:

Purchase the leftmost book. cost[0] = 9.

Purchase the leftmost and rightmost for pairCost = 6.

Purchase the leftmost and rightmost books for pairCost = 6.

The total cost is 9 + 6 + 6 = 21.

'''
import collections

def getMinCost(cost, pairCost, k):
    n = len(cost)
    if n == 0:
        return 0
    
    cost.sort()
    
    l, r = 0, n - 1
    total_cost = 0
    
    # We have k chances to pair the most expensive books
    while k > 0 and l < r:
        # Compare using a pair deal vs buying the two most expensive books individually
        if pairCost < cost[r] + cost[r-1]:
            # It's a good deal. Use pairCost.
            total_cost += pairCost
            r -= 2 # Two most expensive books are bought
            k -= 1 # Used one deal
        else:
            # The pair deal is not worth it for even the most expensive pair.
            # So, no pair deal will ever be worth it. Stop trying to pair.
            break
            
    # Add the costs of all remaining books, which must be bought individually.
    while l <= r:
        total_cost += cost[l]
        l += 1
    
    return total_cost
    
# Test cases
if __name__ == "__main__":
    assert getMinCost([1, 2, 3], 2, 1) == 3
    assert getMinCost([1, 1, 1], 2, 1) == 3
    assert getMinCost([9, 11, 13, 15, 17], 6, 2) == 21
    assert getMinCost([5, 10, 15], 20, 1) == 25
    assert getMinCost([10, 20, 30], 25, 2) == 35
    print(" 😎 All test cases passed ")