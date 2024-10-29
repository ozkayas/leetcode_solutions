from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Will store indices of elements in `nums`
        ans = []

        for i in range(len(nums)):
            # Remove elements not in the current sliding window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove all elements smaller than the current element from the deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add the current element index
            q.append(i)

            # Append the maximum element of the current window to the answer list
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans
