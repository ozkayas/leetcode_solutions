class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # holds each value with its index: {2:0, 7:1, 11:2, 15:3}
        pairMap = dict()

        for i, n in enumerate(nums):
            pairOfN = target - n

            if pairOfN in pairMap:
                return[pairMap[pairOfN], i]
            else:
                pairMap[n] = i

    
        