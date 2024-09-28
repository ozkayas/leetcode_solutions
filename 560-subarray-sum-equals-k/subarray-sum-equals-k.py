class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        pf = 0
        count = 0

        for n in nums:
            pf += n
            if pf == k:
                count += 1
            if (pf-k) in f:
                count += f[pf-k]
            f[pf] += 1
    
        return count


        

        