"""
Your project team needs to work closely with a group of software testers. They have requested that your team create an array generator service to assist with testing software functionality. Create an array generator service.

Its input parameters are:

arr[n] contains n positive integers.
state is a string that contains n characters.
Each character is a '0' or '1'.
If state[i] = '1', arr[i] is available.
If state[i] = '0', arr[i] is blocked.
To create an integer array, S, the following operation is performed exactly m times. S is initially empty.

Choose any arr[i] that is available, that is, where state[i] = '1', the same element can be chosen any number of times.
Append the value in arr[i] to S.
For all state[i] = '0' such that state[i-1] = '1', change state[i] to '1'. For example, if state = '0100101' before the operation, it equals '0110111' after the operation.
Find the lexicographically largest sequence S that can be obtained after m operations.

Note: A sequence x of length m is lexicographically larger than sequence y of length m if there exists such i (0 ≤ i < m), that x[i] > y[i], and for any j (0 ≤ j < i) x[j] = y[j].

Example 1:

Input:  arr = [5, 3, 4, 6], state = "1100", m = 5
Output: [5, 5, 6, 6, 6] 
"""
import heapq
from heapq import heappop, heappush
from typing import List


class Solution:

    def updateState(self, states: List[int]) -> List[int]:
        updatedIndexes = []
        for i in range(1, len(states)):
            if states[i] == 0 and states[i-1] == 1:
                updatedIndexes.append(i)
        for i in updatedIndexes:
            states[i] = 1
        return updatedIndexes

    def generateArray(self, arr: List[int], state: str, m: int) -> List[int]:
        ans = []
        # list representation of state string
        states = [int(ch) for ch in state]

        # will hold (-1, -5) (-1, -3) (0, -4) (0, -6) as tuples to get 1 -> with max value
        # Lets just add values with state 1 not 0
        maxHeap = []
        # Initialize heap with first state
        for i, n in enumerate(arr):
            if states[i] == 1:
                maxHeap.append(-n)

        heapq.heapify(maxHeap)

        # while maxHeap:
        #     print(heappop(maxHeap))

        for _ in range(m):
            # find max value with state 1
            maxValue = maxHeap[0]
            ans.append(-maxValue)
            # Update state, get newly updated indexes from 0 to 1
            updatedIndexes = self.updateState(states)

            # Update heap
            for idx in updatedIndexes:
                heappush(maxHeap, -arr[idx])

        return ans


print(Solution().generateArray([5,3,4,6], "1100", 5))