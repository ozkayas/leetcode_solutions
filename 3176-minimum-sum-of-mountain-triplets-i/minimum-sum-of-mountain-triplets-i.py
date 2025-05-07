class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        '''        # for each top point, what is the min on left and min on right
                # Then check for each top point if it is a mountain
                # [5,4,8,7,10,2] - loop [1,n-1] range
                #  5,4,4,4,4,2
                #  2,2,2,2,2,2
        '''
        def getMonoStack(nums:List[int]) -> List:
            minlist = []
            curMin = nums[0]
            for n in nums:
                if n < curMin:
                    curMin = n
                minlist.append(curMin)
            return minlist

        monoLeft = getMonoStack(nums)
        monoRight = list(reversed(getMonoStack(list(reversed(nums)))))
        # print(monoLeft)
        # print(monoRight)
    
        output = float('inf')
        for i in range(1, len(nums)-1):
            # This index is not the top of a mountain
            if monoLeft[i] >= nums[i] or monoRight[i] >= nums[i]:
                continue

            curVal = monoLeft[i] + nums[i] + monoRight[i]
            output = min(output, curVal)

        return -1 if output == float('inf') else output









        