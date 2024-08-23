class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mn = mx = nums[0]
        for n in nums:
            mn = min(mn, n) # 1 -> mn - mn
            mx = max(mx, n) # 5 -> mx - mn
    
        N = mx - mn + 1
        
        cntArr = [0 for i in range(N)]

        for n in nums:
            idx = n - mn
            cntArr[idx] += 1
        
        ans = []
        for i, freq in enumerate(cntArr):
            if freq!= 0:
                for _ in range(freq):
                    ans.append(i + mn)
        
        return ans


        