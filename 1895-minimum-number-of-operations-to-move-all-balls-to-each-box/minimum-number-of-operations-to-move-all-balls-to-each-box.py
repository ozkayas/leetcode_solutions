class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        answer = [0 for _ in range(N)]
        ballToAdd , ballsCarried = 0, 0
        for i in range(N):
            answer[i] += ballToAdd
            ballsCarried += int(boxes[i]) 
            ballToAdd += ballsCarried

        ballToAdd , ballsCarried = 0, 0
        for i in range(N-1,-1,-1):
            answer[i] += ballToAdd
            ballsCarried += int(boxes[i]) 
            ballToAdd += ballsCarried

        # print(answer)
        return answer
        

'''
Approach 2: Sum of Left and Right Moves
Intuition
From the previous approach, observe that a ball can move in only one direction: either left or right. If the target box is to the left of the ball, it will move left. If the target box is to the right of the ball, it will move right. So, for each box, some balls will come from the left side, and others will come from the right side.

To calculate the distances for all the balls coming from the left in just one pass, we use a combined approach within a single loop. As we iterate through the boxes from left to right, we keep track of how many balls we’ve encountered so far using the variable ballsToLeft. Each time we move to the next box, the distance for all the balls we’ve passed increases by one. So, the total number of operations for those balls increases by the number of balls we've encountered up to that point. We also keep track of the cumulative number of moves using the variable movesToLeft.

Similarly, we calculate the distances for the balls coming from the right by iterating through the boxes from right to left. This is achieved using the variable ballsToRight to track how many balls we’ve encountered, and movesToRight to track the cumulative moves. During this reverse pass, we simultaneously calculate and accumulate the number of moves required for balls coming from the right.

In each iteration, we update the answer array by adding the moves calculated from both the left and right sides. The value for each box in answer[i] (for the left pass) and answer[j] (for the right pass) represents the total moves required for balls to reach that box.

At the end of the loop, the answer array will contain the total number of moves for each box, and we return this array.

Algorithm
Initialize n as the length of the boxes string and create an array answer to store the result.

Initialize variables ballsToLeft, movesToLeft, ballsToRight, and movesToRight to track the number of balls and the moves required to move balls to the left and right, respectively.

Single pass through the string boxes:

For each index i:
Left pass (first half of the loop):

Add the current number of moves to the left (movesToLeft) to the corresponding index in the answer array.
Update ballsToLeft by adding the number of balls in the current box.
Update movesToLeft by adding ballsToLeft (total balls to the left) to account for the moves required for the next balls.
Right pass (second half of the loop):

Calculate the corresponding index j for the right pass (n - 1 - i).
Add the current number of moves to the right (movesToRight) to the corresponding index in the answer array.
Update ballsToRight by adding the number of balls in the current box.
Update movesToRight by adding ballsToRight (total balls to the right) to account for the moves required for the next balls.
Return the answer array containing the minimum number of operations for each box.
'''