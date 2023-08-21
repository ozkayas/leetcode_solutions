class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0 
        jewelSet = set()
        for i in range(len(jewels)):
            jewelSet.add(jewels[i])

        for i in range(len(stones)):
            if stones[i] in jewelSet:
                count += 1

        return count