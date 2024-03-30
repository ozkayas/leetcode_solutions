class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        # Using the method discussed on editorial
        def atMostK(kk):
            l = ans = 0
            hM = dict()

            for r, n in enumerate(nums):
                hM[n] = 1 + hM.get(n,0)

                while len(hM) > kk:
                    hM[nums[l]] -= 1
                    if hM[nums[l]] == 0:
                        del hM[nums[l]]                    
                    l += 1
                ans += (r-l+1)
            return ans

        return atMostK(k) - atMostK(k-1)
