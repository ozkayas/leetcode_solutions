class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMostK(kk):
            l = ans = 0
            hM = dict()

            for r, n in enumerate(nums):
                hM[n] = 1 + hM.get(n,0)
                # print('1.',hSet,l,r,ans)

                while len(hM) > kk:
                    hM[nums[l]] -= 1
                    if hM[nums[l]] == 0:
                        del hM[nums[l]]                    
                    l += 1
                    # print('2.',hSet,l,r,ans)
                ans += (r-l+1)
            return ans

        # print(atMostK(k))
        # print(atMostK(k-1))

        return atMostK(k) - atMostK(k-1)










''' 
               r
      [1,2,1,3,4], k = 3 
             l
      
 s :   1,2 2 3 3
         3 2 2
                           
                           
                           1213 - 213 - 134
           r
      [1,2,1,2,3], k = 2
       ---
       -----
    

s :    1 2 2
         


12 
      
'''