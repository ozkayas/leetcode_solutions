class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pfSum = 0
        seen = dict()
        # index degerini de tutmamiz lazim, cunku subarr min len >=2 olacak, bunu kontrol etmeliyiz
        for i, n in enumerate(nums):
            pfSum += n
            pfSum %= k
            # if cur == 0 and not first element => true
            if pfSum == 0 and i > 0:
                return True
            if pfSum in seen:
                if i - seen[pfSum] > 1:
                    return True
            else:
                seen[pfSum] = i
        
        return False


        