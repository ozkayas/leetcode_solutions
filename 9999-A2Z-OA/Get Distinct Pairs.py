# https://www.geeksforgeeks.org/count-distinct-pairs-with-given-sum/
# https://www.fastprep.io/problems/amazon-get-distinct-pairs
'''
A financial analyst for Amazon Web Services (AWS) is responsible for a portfolio of profitable stocks represented in an array. Each item in the array represents the yearly profit of a corresponding stock. The Amazonian gathers all distinct pairs of stocks that reached the target profit. Distinct pairs are pairs that differ in at least one element. Given the array of profits, find the number of distinct pairs of stocks where the sum of each pair's profits is exactly equal to the target profit.

Function Description

Complete the function getDistinctPairs in the editor.

getDistinctPairs has the following parameter(s):

1. int stocksProfit[n]: an array of integers representing the stocks profits
2. target: an integer representing the yearly target profit
Returns

int: the total number of pairs determined

Example 1:

Input:  stocksProfit = [5, 7, 9, 13, 11, 6, 6, 3, 3], target = 12
Output: 3 
Explanation:

There are 4 pairs of stocks that have the sum of their profits equals to the target 12. Note that because there are two instances of 3 in stocksProfit there are two pairs matching (9, 3): stocksProfits indices 2 and 7, and indices 2 and 8, but only one can be included.
   
There are 3 distinct pairs of stocks: (5, 7), (3, 9), and (6, 6) and the return value is 3.

      
Constraints:
1 ≤ n ≤ 5 x 105
0 ≤ stocksProfit[i] ≤ 109
0 ≤ target ≤ 5 x 109

'''


# pairs, target = [5, 6, 5, 7, 7, 8], 13 #ans = 2
pairs, target = [5, 7, 9, 13, 11, 6, 6, 3, 3], 12 # ans = 3

hM = dict()
ans = set()

for n in pairs:
    if (target - n) in hM:
        ans.add((target-n,n))
    hM[n] = 1 + hM.get(n,0)

print(len(ans))