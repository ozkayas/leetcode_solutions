"""
https://www.fastprep.io/problems/amazon-get-max-aggregate-temperature-change

Alexa is Amazon's virtual AI assistant. It makes it easy to set up your Alexa-enabled devices, listen to music, get weather updates, and much more. The team is working on a new feature that evaluates the aggregate temperature change for a period based on the changes in temperature of previous and upcoming days.

Taking the change in temperature data of n days, the aggregate temperature change evaluated on the ith day is the maximum of the sum of the changes in temperatures until the ith day, and the sum of the change in temperatures in the next (n - i) days, with the ith day temperature change included in both.

Given the temperature data of n days, find the maximum aggregate temperature change evaluated among all the days.

Function Description

Complete the function getMaxAggregateTemperatureChange in the editor.

getMaxAggregateTemperatureChange has the following parameter:

int tempChange[n]: the temperature change data of n days
Returns

long: the maximum aggregate temperature change

Example 1:

Input:  tempChange = [6, -2, 5]
Output: 9
Explanation:

The aggregate temperature change on each day is evaluated as:



For day 1, there are no preceding days info, but the day itself is included in the calculation. Temperature changes = [6] for the before period.

For succeeding days, there are values [6, -2, 5] and 6 + (-2) + 5 = 9.

Again, the chagne for day 1 is included. The maximum of 6 and 9 is 9.

For day 2, consider [6, -2] -> 6 + (-2) = 4, and [-2, 5] -> (-2) + 5 = 3. The maximum of 3 and 4 is 4.

For day 3,consider [6, -2, 5] -> 6 + (-2) + 5  = 9, and [5]. The maximum of 9 and 5 is 9.

The max aggregate temp change is max (9, 4, 9) = 9.

Example 2:

Input:  tempChange = [-1, 2, 3]
Output: 5
Explanation:

Explanation hasn't been found yet. If you happen to know about it, feel free to lmk! Manyyy thanks in advance! 💜

Constraints:
1 <= n <= 105
-109 <= tempChange[i] <= 109 where, 1 <= i <= n


"""
nums = [6, -2, 5, 7 ]

preFix = 0
postFix = 0
left = []
right = []


for n in nums:
    preFix += n
    left.append(preFix)
    
    
for n in nums[::-1]:
    postFix += n
    right.append(postFix)

right.reverse()

# print(left)
# print(right)
print(max(max(left), max(right)) )


'''
       9  3  5
       6  4  9

    0  6 -2  5  
       |   
      6,9
          |
         4,3
             |
            9,5
                
'''