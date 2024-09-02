class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        N = len(nums)
        # use monotonic stack from both sides to keep track the min at left for each index
        # [8, 6, 1, 1, 1] and [1, 1, 3, 3, 3]
        leftMin = deque([nums[0]])
        rightMin = deque([nums[-1]])
        minn = nums[0]
        for i in range(1, N):
            if nums[i] < minn:
                minn = nums[i] 
            leftMin.append(minn)
        
        minn = nums[-1]
        for i in range(N-1, 0, -1):
            if nums[i] < minn:
                minn = nums[i] 
            rightMin.appendleft(minn)
        # print(f"leftMin: {leftMin}")
        # print(f"rightMin: {rightMin}")

        ans = float('inf')
        for i in range(1, N-1):
            if leftMin[i] < nums[i] > rightMin[i]:
                ans = min(ans,leftMin[i] + nums[i] + rightMin[i] )


        return -1 if ans == float('inf') else ans

            






        