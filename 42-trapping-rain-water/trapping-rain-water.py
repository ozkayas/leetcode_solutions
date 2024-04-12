class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        N = len(height)
        maxL, maxR = [0 for i in range(N)], [0 for i in range(N)]
        for i in range(1, N):
            maxL[i]=(max(maxL[i-1],height[i-1])) 
        for i in range(N-2, -1, -1):
            maxR[i]=(max(maxR[i+1],height[i+1])) 
        
        print(maxL)
        print(maxR)

        for i in range(N):
            cur = min(maxL[i],maxR[i]) - height[i]
            if cur > 0:
                ans += cur
        return ans

        