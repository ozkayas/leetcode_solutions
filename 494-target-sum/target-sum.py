class Solution:
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = dict()

        def backT(nums, target, curSum):
            if len(nums) == 0:
                if target == 0:
                    curSum += 1
                return curSum

            args = tuple(nums+[target])
            if args in memo:
                return memo[args]
            # explore +last element
            lastNum = nums.pop()
            leftSum = backT(nums, target-lastNum, curSum)
            rightSum = backT(nums, target+lastNum, curSum)
            nums.append(lastNum)
            memo[args] = leftSum+rightSum
            return memo[args]


        
        return backT(nums, target, 0)