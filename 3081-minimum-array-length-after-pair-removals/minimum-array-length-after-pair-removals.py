class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        i = 0
        j = N // 2
        removed = 0

        while j < N and i < N//2:
            if nums[i] < nums[j]:
                removed += 2
                i += 1
            j += 1
        
        return N - removed


"""
1 3 3 3 3 3 4
i     j
  i         j  

1 3 3 3 3 4
i     j
  i       j  

2 3 4
i j

"""