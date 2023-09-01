class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        ans = min( height[l], height[r] ) * (r-l)

        while l < r:
            # print('ans before shifting: ',ans)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            # print('shifting... l: ',l ,"r: ",r)
            ans = max(ans, min( height[l], height[r] ) * (r-l))
            # print('ans after shifting: ',ans)
            # print('-----------------')

            
        return ans
