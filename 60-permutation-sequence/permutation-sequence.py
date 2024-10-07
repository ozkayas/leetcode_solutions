class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = []
        def fillAns(nums: list, k:int) -> str:
            nonlocal ans
            N = len(nums)
            if N == 1: 
                ans.append(str(nums[0]))
                return

            # 6 for 1234
            blockSize = int(math.factorial(N-1))
            # 1-6/7-12/13-18/19-24 
            bucketNo = k // blockSize # -> 1 -> 7-12 araligi
            ans.append(str(nums.pop(bucketNo)))
            fillAns(nums, k % blockSize)

        k-=1

        fillAns(list(range(1,n+1)),k)
        return "".join(ans)

        


        
        