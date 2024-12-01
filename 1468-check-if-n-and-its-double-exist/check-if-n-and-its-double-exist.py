class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numSet = set()

        for num in arr:
            if num*2 in numSet or num/2 in numSet:
                return True
            
            numSet.add(num)
        return False
        