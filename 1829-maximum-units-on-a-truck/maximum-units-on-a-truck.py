class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # sort according to capacity, decreasing
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        units = 0
        for box,unit in boxTypes:
            # If We can load all of this box type
            if box <= truckSize:
                units += box * unit
                truckSize -= box
            else: # Truck is about to be fully loaded
                units += truckSize * unit
                break
            
        return units
