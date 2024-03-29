class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l,r, ans = 0, 0, 0
        N =  len(nums)
        m = dict()

        while r < N:
            curR = nums[r]
            m[curR] = 1 + m.get(curR, 0)
            if m[curR] > k:
                while l < r and m[curR] > k:
                    m[nums[l]] -= 1
                    l += 1
            else:
                ans = max(ans, (r-l+1))
                # print(r-l+1)
            r+=1

        return ans

        
'''          r
        [1,4,4,3].    k = 1
         l
  hMap :
      1: 1 
      4: 2
      3: 
  

   ans : 1,   

   // r nin bulundugu degerdeki fazlalik azalana kadar l yi saga shift et, while ile ve '''