'''
In one of the warehouses of Amazon, a pan balance is used to weigh and load the parcels for delivery.

A pan balance has 2 pans, and each of the pans can contain one parcel. Due to some defect, one of the pans shows an extra erroneous weight wt. A pair of parcels is said to be balanced if they show the same weight on the pan balance. Since one of the pans is heavier by the amount wt, the absolute difference in weight of the parcels has to be wt.

Given the weights of n parcels, weight[n], and the erroneous weight wt, find the number of ways to group these parcels into pairs such that every pair of the group is balanced. Since the answer can be large, compute it modulo (109 + 7). Technically, the task is to find out the number of pairs that can be formed from the weight array which have an absolute difference equal to wt. If there are no such pairs, you have to return 0.

Note:

A parcel cannot be present in more than one pair in a group.
Two groups are different if at least one of their pairs contains a different pair of parcels. The pairs at indices (i, j) and (j, i) are considered the same.
If there are no such pair, you have to return 0.
Function Description

Complete the function numberOfWaysToGroupParcels in the editor.

numberOfWaysToGroupParcels has the following parameters:

int weight[n]: an array of integers representing the weights of the parcels
int wt: the erroneous weight shown by one of the pans
Returns

int: the number of ways to group the parcels into balanced pairs modulo (109 + 7)

Example 1:

Input:  weight = [4, 5, 5, 4, 4, 5, 2, 3], wt = 1
Output: 6 
Explanation:

Pairs will contain either 4 and 5 or 2 and 3 with an absolute difference of 1.

All possible ways of grouping the parcels into pairs are, {(1, 2), (4, 3), (5, 6), (7, 8)}, {(1, 3), (4, 2), (5, 6), (7, 8)}, {(1, 6), (4, 3), (5, 2), (7, 8)}, {(1, 2), (4, 6), (5, 3), (7, 8)}, {(1, 3), (4, 6), (5, 2), (7, 8)} and {(1, 6), (4, 2), (5, 3), (7, 8)}. In all these groups, the absolute difference of the weights of each pair of parcels is equal to the given extra weight wt = 1. For example, consider the group {(1, 6), (4, 2), (5, 3), (7, 8)}.
'''

'''
Soru net degil ama sanirim bu sekilde.
frekans map olustur
keyleri sort et ve olasi pairleri cikart
4:3 , 5:3, 2:1, 3:1  --> pairlerin frekanslari ayni olmali, deiglse 0 don, ortada eleman kaliyor cunku
olasi pairler: (2,3), (4,5) bunlarin frekanslari (1,1)(3,3) -> 1! x 3! kendi iclerindeki eslesme kombinasyonlari x her biri
(2,2)(4,4) olsaydi 2! x 4! olacakti
'''

from collections import Counter
import math


def fn(weight, wt) -> int:
    freq = Counter(weight)
    addedToPairs = set()
    pairs = set()
    keys = sorted(list(freq.keys()))


    for key in keys:
        if key in addedToPairs:
            continue

        pairOfKey = key + wt

        if pairOfKey not in keys: # Return 0 , no pair 
            return 0
        
        addedToPairs.add(key, )
        addedToPairs.add( pairOfKey)
        pairs.add((key, pairOfKey))
        print(pairs)

    # check if all keys are paired
    if len(addedToPairs) != len(keys):
        return 0
    
    # Start calculating answer
    ans = 1
    MOD = 1e9 + 7
    for a,b in pairs:
        if freq[a] != freq[b]:
            return 0
        ans = (ans * math.factorial(freq[a]) % MOD) % MOD
        
    return int(ans)

print(fn([4, 5, 5, 4, 4, 5, 2, 3], 1))
print(fn([4, 5, 5, 4, 4, 5, 2, 3, 2, 3], 1))
print(fn([4, 6, 4, 6, 4, 6, 1, 3, 1, 3, 7, 9, 7,9],wt = 2))
