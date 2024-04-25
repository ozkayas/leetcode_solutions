class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMost(kk:int) -> int:
            l, r = 0, 0
            hMap = defaultdict(int)
            counter = 0

            while r < len(nums):
                hMap[nums[r]] += 1

                ## if len > kk , shrink window
                while len(hMap) > kk:
                    hMap[nums[l]] -= 1
                    if hMap[nums[l]] == 0:
                        del hMap[nums[l]]
                    l += 1

                counter += (r-l) + 1
                r += 1
            return counter


        return atMost(k) - atMost(k-1)
        
'''        # Using the method discussed on editorial
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

        return atMostK(k) - atMostK(k-1)'''
