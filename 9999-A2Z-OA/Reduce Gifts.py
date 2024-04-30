'''New Year's Day is around the corner and Amazon is having a sale. 
They have a list of items they are considering but they may need to remove some of them. 
Determine the minimum number of items to remove from an array of prices so that the sum of prices of any 
k items does not exceed a threshold.

Note: If the number of items in the list is less than k, then there is no need to remove any more items.'''

# https://www.fastprep.io/problems/amazon-reduce-gifts
# Similar problem : 
# https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

# INPUT
# prices = [3, 2, 1, 4, 6, 5] 
# k = 3
# threshold = 14

prices= [10, 8, 12, 15, 20, 5]
k= 3
threshold= 25

prices.sort()
ans = 0

while len(prices) > k:
    sum_last_k = sum(prices[-k:])
    if sum_last_k > threshold:
        prices.pop()
        ans += 1
    else:
        break #found a solution just break the loop

print(ans)
