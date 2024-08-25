'''The supply chain manager at one of Amazon's warehouses is shipping the last container of the day. 
All n boxes have been loaded into the truck with their sizes represented in the array boxes. 
The truck may not have enough capacity to store all the boxes though, so some of the boxes may have to be unloaded. 
The remaining boxes must satisfy the condition max(boxes) ≤ capacity * min(boxes).

Given the array, boxes, and capacity, find the minimum number of boxes that need to be unloaded.

Function Description

Complete the function getMinimumBoxes in the editor.

getMinimumBoxes has the following parameters:

1. int[] boxes: an array of integers representing the sizes of the boxes
2. int capacity: the capacity of the truck
Returns

int: the minimum number of boxes that need to be unloaded

Example 1:

Input:  boxes = [1, 4, 3, 2], capacity = 2
Output: 1 '''



'''
1 2 3 4
l     r

'''
from typing import List

class Solution:

    memo = set()
    ans = float("inf")

    def isValid(self,capacity:int, low:int, high:int):
        # print("isValid", low, high)
        return high <= capacity * low

    def unloadedBoxCount(self,l:int, r:int, N:int):
        inTruck = r - l + 1
        return N - inTruck


    def nextLeftIndex(self,lastIdx:int, boxes:List[int]):
        i = lastIdx
        while i < len(boxes) and boxes[i] == boxes[lastIdx]:
            i += 1
        print(f"lastIndex: {lastIdx}, nextIndex: {i}")
        return i
    
    def nextRightIndex(self,lastIdx:int, boxes:List[int]):
        i = lastIdx
        while i > 0 and boxes[i] == boxes[lastIdx]:
            i -= 1
        print(f"lastIndex: {lastIdx}, nextIndex: {i}")
        return i




    def rec(self,capacity, l,r,boxes):
        N = len(boxes)
        if l > r or r < 0 or l > N-1:
            return

        # We already checked this, memoization
        if (l,r) in self.memo:
            return 
        else:
            self.memo.add((l,r))
        print("call rec for array", boxes[l:r+1])

        if self.isValid(capacity,boxes[l],boxes[r]):
            self.ans = min(self.ans, self.unloadedBoxCount(l, r, len(boxes)))
            print(f"Found answer {self.ans} for subarray {boxes[l:r+1]}")
            return
        
        self.rec(capacity, self.nextLeftIndex(l, boxes), r,boxes)
        self.rec(capacity, l, self.nextRightIndex(r, boxes), boxes)


    def getMinimumBoxes(self,capacity: int, boxes: List[int]):
        N, l, r = len(boxes), 0, len(boxes)-1
        boxes.sort()
        self.rec(capacity, l, r, boxes)
        return self.ans


# print("RESULT",Solution().getMinimumBoxes( 2,[1,4,2,3]))
print("RESULT",Solution().getMinimumBoxes( 1,[8, 4, 5, 3, 7])) ## result: 4
# print("RESULT",Solution().getMinimumBoxes( 3,[10, 2, 6, 5, 4])) ## result: 1
# print("RESULT",Solution().getMinimumBoxes( 1, boxes = [7, 7, 7, 7])) ## result: 0
# print("RESULT",Solution().getMinimumBoxes( 2, boxes =[2, 2, 2, 5, 5, 7, 7] )) ## result: 3 




