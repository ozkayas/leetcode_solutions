class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        s = mx = mn = -1
        ans = 0

        for i, n in enumerate(nums):
            if n < minK or n > maxK:
                s = mn = mx = i
            if n == minK:
                mn = i
            if n == maxK:
                mx = i
            
            possible_subarrays = min(mx,mn)-s
            ans += possible_subarrays
            # print(i,possible_subarrays, ans)

        
        return ans

            





'''
               s
                         i   
    [1,3,5,2,7,5,1,3,4,5,1] 
                       x  
                         m  
       
         1-3-5      

         // e out of bound s = x = m e'ye gelsin, e++
       
       
       
       
'''