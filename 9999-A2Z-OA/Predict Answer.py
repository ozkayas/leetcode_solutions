'''
https://www.fastprep.io/problems/amazon-predict-answer
In this stock price prediction game launched on Amazon Games, Player 1 provides Player 2 with stock market data for n consecutive days, representing Amazon's stock prices on each day, represented by stockData[].

The rules of the game are as follows:

1. Player 1 will tell Player 2 a specific day number i (where 1 ≤ i ≤ n)
2. Player 2 has to find the nearest day j (1 <= j < i or i < j <= n) in the past or future, on which the stock price was lower than on the given day, i.e., stockData[j] < stockData[i]
3. If there are more than one j which satisfies Rule 2, then Player 2 will find the day number which is smaller. (i.e. the smallest j satisfying Rule 2)
4. If no such day j exists, then answer for that case is -1
Given q queries in the array queries, the task is to find the answer for each queries[i] in the queries and return a list of answer as per the above rules corresponding to each query.

Note: The description and the answer format both adhere to 1-based indexing for the arrays. (Please see the below Example for better understanding :)

Function Description

Complete the function predictAnswer in the editor.

predictAnswer has 2 parameters:

int stockData[n]: an integer array denoting the value of each stockData[i] is the stock price on the i-th day (where 0 ≤ i < n)
int queries[q]: an integer array denoting the value of each element queries[i] is the day number given in the query (where 0 ≤ i < q)
Returns

int[]: an integer array denoting the value at each index i is the answer to queries[i]

Thank you soooo much for sharing the source! All the credit goes to our incredible friend who made it possible! You’re the real MVP! 👑

Example 1:

Input: stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4], queries = [6, 5, 4]
Output: [5, 4, 8]
Explanation:


On day 6, the stock price is 10. Both 9 and 8 are lower prices one day away. Choose 9 (day 5) because it is before day 6.

On day 5, the stock price is 9. 4 is the closest lower price on day 4.

On day 4, the stock price is 4. The only lower price is on day 8.

So, the output is [5, 4, 8].
      
Constraints:
1 ≤ n ≤ 10^5
1 ≤ stockData[i] ≤ 10^9
1 ≤ q ≤ 10^5
1 ≤ queries[j] ≤ n'''

def predictAnswer(stockData, queries):
    smallerOnLeft = [-1] * len(stockData)
    smallerOnRight = [-1] * len(stockData)
    stack = [] # Monotonic stack, will hold values and their indices (value, index)
    for i in range(len(stockData)):
        while stack and stack[-1][0] >= stockData[i]:
            stack.pop()
        if stack:
            smallerOnLeft[i] = stack[-1][1] + 1
        stack.append((stockData[i], i))

    stack = []  # Reset stack for right side
    for i in range(len(stockData) - 1, -1, -1):
        while stack and stack[-1][0] >= stockData[i]:
            stack.pop()
        if stack:
            smallerOnRight[i] = stack[-1][1] + 1
        stack.append((stockData[i], i))
    result = []
    for query in queries:
        index = query - 1
        left = smallerOnLeft[index]
        right = smallerOnRight[index]
        if left == -1 and right == -1:
            result.append(-1)
        elif left == -1:
            result.append(right)
        elif right == -1:
            result.append(left)
        else:
            result.append(left if left < right else right)
    return result

        

# Test cases
if __name__ == "__main__":
    assert predictAnswer([5, 6, 8, 4, 9, 10, 8, 3, 6, 4], [6, 5, 4]) == [5, 4, 8]
    assert predictAnswer([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) ==  [-1, 1, 2, 3, 4]
    print(" 😎 All test cases passed! 😎 \n")
  