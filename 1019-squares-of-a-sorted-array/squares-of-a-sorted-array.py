class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return [nums[0]**2]
        s, e = 0 , len(nums)-1
        res = []

        while s <= e:
            if abs(nums[s]) > abs(nums[e]):
                res.append(nums[s]**2)
                s += 1

            else:
                res.append(nums[e]**2)
                e -= 1
        
        return reversed(res)