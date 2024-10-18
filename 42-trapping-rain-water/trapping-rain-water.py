class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        leftMax = [0 for _ in range(N)]
        rightMax = [0 for _ in range(N)]
        prev = 0
        for i in range(N):
            leftMax[i] = prev
            prev = max(prev, height[i])
        prev = 0
        for i in range(N-1, -1, -1):
            rightMax[i] = prev
            prev = max(prev, height[i])
        
        print(leftMax)
        print(rightMax)
        ans = 0
        for i in range(N):
            lowBound = min(leftMax[i], rightMax[i])
            rain = lowBound - height[i]
            if rain > 0:
                ans += rain
        return ans
        