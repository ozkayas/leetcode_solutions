class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        preSumDic = defaultdict(int)
        preSumDic[0] = 1
        prev = 0

        ans = 0

        for n in nums:
            prev += n
            prev %= k
            if prev in preSumDic:
                ans += preSumDic[prev]
            
            preSumDic[prev] += 1


        return ans




        


# [4, 5, 0, -2, -3, 1], k = 5
#  4  4  4   2   4  0
