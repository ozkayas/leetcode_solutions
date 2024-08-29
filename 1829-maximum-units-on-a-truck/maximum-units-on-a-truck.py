class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        ans = 0
        # sort boxes according to i[1]
        boxTypes.sort(key = lambda item:item[1], reverse = True)
        # print(boxTypes)

        for boxT in boxTypes:
            if truckSize == 0:
                break
            # truck has capacity to take all this boxType
            if truckSize >= boxT[0]:
                ans += boxT[0] * boxT[1]
                truckSize -= boxT[0]
            else:
                ans += truckSize * boxT[1]
                truckSize = 0

        return ans


        
        