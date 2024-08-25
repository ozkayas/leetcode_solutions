'''Amazon has recently established n distribution centers in a new location. 
They want to set up 2 warehouses to serve these distribution centers. 
Note that the centers and warehouses are all built along a straight line. 
A distribution center has its demands met by the warehouse that is closest to it. 
A logistics team wants to choose the location of the warehouses such that the sum of the distances of the distribution centers to their closest warehouses is minimized.

Given an array dist_centers, that represent the positions of the distribution centers, return the minimum sum of distances to their closest warehouses if the warehouses are positioned optimally.

Function Description

Complete the function getMinTotalDistance in the editor.

getMinTotalDistance has the following parameter:

int dist_centers[n]: the locations of the distribution centers
Returns

int: the minimum sum of distances

Example 1:

Input:  dist_centers = [1, 2, 3]
Output: 1 
Explanation:

One optimal solution is to position the 2 warehouses at x1 = 1 and x2 = 2.'''

from typing import List

class Solution:

    memo = set()
    min_total_dist = float('inf')

    # Assigns the center to the nearest warehouse
    def assignCentersToWH(self, l:int, r:int, centers:List[int]) -> dict[int,int]:
        assignMap = dict()
        for center in centers:
            if abs(center-centers[l]) <= abs(center-centers[r]):
                assignMap[center] = centers[l]
            else:
                assignMap[center] = centers[r]
        return assignMap

    def totalDistanceFromAssignMap(self, assignMap: dict[int,int]) -> int:
        totalDistance = 0
        for center, wh in assignMap.items():
            totalDistance += abs(center - wh)

        return totalDistance

    def dp(self,l:int, r:int, centers: List[int]):
        # visited and evaluated already
        if (l,r) in self.memo:
            return

        self.memo.add((l,r))
        
        assignMap = self.assignCentersToWH(l, r, centers)
        totalDistanceForThisState = self.totalDistanceFromAssignMap(assignMap)
        if totalDistanceForThisState < self.min_total_dist:
            self.min_total_dist = totalDistanceForThisState
            print(f"found a minima at {l} - {r}")

            self.dp(l + 1, r, centers)
            self.dp(l, r -1, centers)

        # if the found distance is not getting better, do not continue in this direction
        else:
            return

        

    def getMinTotalDistance(self,dist_centers: List[int]) -> int:
        if len(dist_centers) < 3: return 0
        dist_centers.sort()

        self.dp(0, len(dist_centers)-1, dist_centers)

        return self.min_total_dist



# print("RESULT", Solution().getMinTotalDistance([1,2,3]))
# print("RESULT", Solution().getMinTotalDistance([1,6]))
# print("RESULT", Solution().getMinTotalDistance([1,2,4,5]))
# print("RESULT", Solution().getMinTotalDistance([1,2,4,5,8,9,10,11,12]))
# print("RESULT", Solution().getMinTotalDistance([1,9,10,11,12]))
print("RESULT", Solution().getMinTotalDistance([1, 5, 22, 25, 26, 100]))
