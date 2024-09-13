"""
Get Max Reward Points 🍐
🤘 INTERN
Amazon shopping periodically has offers to attract more customer.

It recently launched an offer for n items in its inventory, where the ithitem offered reward[i]reward points to the customer purchasing the item. Every time an offer-bearing item is purchased, the customer gains the reward points associated with that item. Then the reward points of the remaining items are reduced by 1 unless it will reduce the points below 0.

Note

Each item can be purchased at most once, in other words, reward[i] becomes0after the ithitem is purchased.

Function Description

Complete the function getMaxRewardPointsin the editor.

getMaxRewardPointshas the following parameter(s):

int reward[n]: the reward points of each item
Returns

long_int: the maximum reward points which can be collected
⋅•⋅⊰∙∘☽ 🎀 Credit to eva 🎀 ☾∘∙⊱⋅•⋅

Example 1:


Input:  reward = [5, 2, 2, 3, 1]
Output: 7
Explanation:


Considering 0-based indexing, the items can be purchased in the following order:

1. First, purchase item 2, points earned = reward[2] = 2. Points of remaining items after this purchase reward = [4, 1, 0, 2, 0].

2. Next, purchase item 3, points earned = reward[3]= 2. Points of remaining items after this purchase reward = [3, 0, 0, 0, 0].

3. Finally, purchase item 0, points earned = reward[0] = 3. Points of remainig items after this purchase reward = [0, 0, 0, 0, 0]

At this point, no items have reward points left. The maximum reward points is 2 + 2 + 3 = 7.

Example 2:


Input:  reward = [5 ,5 ,5]
Output: 12
Explanation:


Using 0-based indexing, the items can be purchased in the following order:

1. First, purchase item 0, points earned = reward[0] = 5. Points of remaining items after this purchase reward = [0, 4, 4].

2. Next, purchase item 1, points earned to = reward [1] = 4. and reward = [0, 0, 3].

3. Finally, purchase item 2, points earned = reward[2] = 3 and reward = [0, 0, 0].

The maximum reward points is (5 + 4 + 3 = 12).

Constraints:
1 <= n <= 105
0 <= reward[i] <= 106
"""
from typing import List

def getMaxRewardPoints(reward:List[int]) -> int:

    reward.sort(reverse=True)
    # how many times we picked a reward,
    # at each iteration the real remainng value of a reward is calculated with these
    counter = 0

    ans = 0

    for rew in reward:
        remainingRew = rew - counter
        # All items are now zero, finish the loop
        if remainingRew <= 0:
            return ans
        # pick this and get remaining rew
        else:
            ans += remainingRew
            counter += 1

    return ans
    
print(getMaxRewardPoints([5, 2, 2, 3, 1]))
print(getMaxRewardPoints([5, 5, 5]))
print(getMaxRewardPoints([5, 4, 2, 3, 1]))

