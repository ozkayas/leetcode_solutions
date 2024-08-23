class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # init deques 
        minDeq = deque([nums[0]])
        maxDeq = deque([nums[0]])


        # returns ans diff of min & max
        def isDiffInLimit() -> bool:
            delta = abs(minDeq[0] - maxDeq[0])
            return delta <= limit
        
        # update deques when window is shrinked or expanded
        def updateDeques(n:int, operation: str):
            if operation == "expand":
                while minDeq and n < minDeq[-1]:
                    minDeq.pop()
                minDeq.append(n)
                while maxDeq and n > maxDeq[-1]:
                    maxDeq.pop()
                maxDeq.append(n)
            # shrinking window
            else:
                if n == minDeq[0]:
                    minDeq.popleft()
                if n == maxDeq[0]:
                    maxDeq.popleft()


        l, r = 0, 0
        maxSubLen = 0

        while r < len(nums):

            if isDiffInLimit():
                maxSubLen = max(maxSubLen, (r-l+1))
                r += 1
                # update min, max while expanding the window
                if r < len(nums):
                   updateDeques(nums[r],"expand") 
            else:
                updateDeques(nums[l],"shrink")
                l += 1

        return maxSubLen


        