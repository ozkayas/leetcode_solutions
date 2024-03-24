class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        N = len(nums)

        def bt(i, perm):            
            cur = nums[i]
            perm.append(cur)
            if len(perm) == N:
                ans.append(perm.copy())
                return


            for j in range(N):
                if nums[j] not in perm:
                    bt(j, perm)
                    perm.pop()

        

        for i in range(N):
            bt(i, [])

        return ans 