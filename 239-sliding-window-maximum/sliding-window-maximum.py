class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1: return nums

        output = []
        window = deque()
        i = 0
        while i < len(nums):
            # popleft if window[0] should be out of window
            if window and window[0] == i-k:
                window.popleft()
            
            # We will append nums[i] but before remove smallers
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
         
            window.append(i)
            # window[0] gives the index of the max value in the current window
            maxIdx = window[0]

            # Skip first k, because the window is not yet constructed
            if i >= k -1:
                output.append(nums[maxIdx])
            i += 1

        return output

        