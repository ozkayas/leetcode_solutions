"""
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

"""
import math

"""
Explanation to myself

preFS:   [1   4   6  10  15]
postFS:  [15  14  11  9  5]

iterate from 0 till -2 index

         [1, 3, 2, 4, 5]
          |
          1-14/4=1-3
             |
             4/2 - 11/3= 2-3
                 |
                 6/3-9/2=2-4
                    |
                    10/4-5/1 = 2-5

"""



# stockPrice = [1, 3, 2, 3]
stockPrice = [1, 3, 2, 4, 5]

prefixSum, postFixSum = [],[]
N = len(stockPrice)
summ = 0
for p in stockPrice:
    summ += p
    prefixSum.append(summ)
summ = 0
for p in reversed(stockPrice):
    summ += p
    postFixSum.append(summ)
postFixSum.reverse()


net_change = []
## Main iteration 
for i in range(N-1): # we do not need the last index
    preAverage = prefixSum[i] // (i+1)
    postAverage = postFixSum[i+1] // (N-i-1)
    net_change.append(abs(preAverage-postAverage))

min_value = min(net_change)

for i in range(len(net_change)):
    if net_change[i] == min_value:
        print("RESULT: ",i+1) 
        break


#### Another way to do it,
# https://github.com/Rohit91singh9/Coding-DP-DSA/blob/main/findEarliestmonth.py
# 1st Approach
def findEarliestMonth(stockPrice):
    # Write your code here
    n = len(stockPrice)
    first = stockPrice[0]
    average_frst = math.floor(first)
    second = sum(stockPrice[1:])
    average_scnd = math.floor(second/(n-1))
    diff = abs(average_frst - average_scnd)
    result = 1
    for i in range(1, n-1):
        first+= stockPrice[i]
        second-= stockPrice[i]
        average_frst = math.floor(first/(i+1))
        average_scnd = math.floor(second/(n-i-1))
        difference_temp = abs(average_frst - average_scnd)
        if(difference_temp<diff):
            diff = difference_temp
            result = i+1
    return result

# 2nd Approach
def findEarliestMonth(stockPrice):
    sum1= 0
    sum2= sum(stockPrice)
    n= len(stockPrice)

    mini= 1000000
    month= 0

    for i in range(0, n-1):
        sum1 += stockPrice[i]
        sum2 -= stockPrice[i]
        avg1= sum1 // (i + 1)
        avg2= sum2 // (n - i - 1)
        if abs(avg2-avg1)< mini:
            mini= abs(avg2-avg1)
            month= i+1
    return month
print(findEarliestMonth([1,3,2,3]))


#3rd Approach
def findEarliestmonth(stockPrice):
    #initialize month variable with 0
    month=0
    change=max(stockPrice)
    l=[]
    while(len(stockPrice)>1):
        l.append(stockPrice.pop(0))
        avg1=sum(l)//len(1)
        avg2=sum(stockPrice)//len(stockPrice)
        if(abs(avg1-avg2)<change):
            change=abs(avg1-avg2)
            month=len(l)
    return month

stockPrice[1,3,2,3]
print("Minimum changes in the month :",findEarliestmonth(stockPrice))