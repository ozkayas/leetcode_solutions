'''
Amazon Shopping is running a reward collection event for its customers.

There are n customers and the i-th customer has collected initialRewards[i] points so far.

One final tournament is to take place where:

The champion earns n additional points
The second place earns n - 1 points
The third place earns n - 2 points
… and the last place earns 1 point
Given an integer array initialRewards of length n, representing the initial reward points of the customers before the final tournament:

Find the number of customers i (1 ≤ i ≤ n) such that, if the i-th customer wins the final tournament, they would have the highest total points.


Note -

The total points = initialRewards[i] + n (if they win). Other customers also get points in the tournament depending on their ranks (from n - 1 to 1). You must check if the i-th customer, upon winning, ends up with the highest total score, regardless of how others place.

Example 1:

Input: initialRewards = [1, 3, 4], n = 3
Output: 2
Explanation:

If the 1st participant wins the final showndown, their total scores would be: 1 + 3 = 4, but this is not the highest possible scores in this scenairo.

For example, if the 3rd participant with an initial earned points of 4 comes 2nd, then they would achieve a total of: 4 + 2 = 6 scores which is higher than 1st participant scores.

If the 2nd participant wins the final showdown, their total points would be: 3 + 3 = 6, and this is the highest total scores in this situation.

Even if the 3rd participant with an initial earned points of 4 comes 2nd, then they would achieve a total of: 4 + 2 = 6 scores which is not greater than 2nd participant scores.

If the 3rd participant wins the final showdown, their total scores would be: 4 + 3 = 7, and this is the highest total scores, as there are no other participants that can achieve the total score of 7 in this case.

Thus, the participants 2 and 3 are the ones such that, if they win the final showdown, they would have the highest total scores.

We return 2 as the output 
      
Example 2:

Input: initialRewards = [5, 7, 9, 11], n = 4
Output: 1
Explanation:

Only the 4th participant is the one who, if they secure victory in the final round, would achieve the highest overall score.
        
Example 3:

Input: initialRewards = [8, 10, 9], n = 3
Output: 2
Explanation:
'''

def countPossibleWinners(initialRewards, n):
    max_initial = max(initialRewards)
    winners_count = 0
    
    for reward in initialRewards:
        if reward + n >= max_initial + (n - 1):
            winners_count += 1
            
    return winners_count


## TEST CASES
if __name__ == "__main__":
    assert countPossibleWinners([1, 3, 4], 3) == 2
    assert countPossibleWinners([5, 7, 9, 11], 4) == 1
    assert countPossibleWinners([8, 10, 9], 3) == 2
    print(" 😎 All test cases passed \n")