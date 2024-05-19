class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort box types
        boxTypes.sort(key = lambda i:i[1])
        # print(boxTypes)

        ans = 0

        while truckSize > 0 and boxTypes:
            lastTypeSize, unit = boxTypes.pop()

            # If truck can take all
            if truckSize >= lastTypeSize:
                ans += lastTypeSize * unit
                truckSize -= lastTypeSize
            # Fill remaining small capacity with this
            else:
                ans += truckSize * unit
                truckSize = 0
            
        return ans

        