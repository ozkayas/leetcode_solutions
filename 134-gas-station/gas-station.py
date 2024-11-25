class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if total gas is equal or > than costs.
        if sum(cost) > sum(gas):
            return -1

        # Start from beginning and try to reach end, 
        # if can and since sum(gas) = sum(cost), can complete cycle
        N = len(gas)
        currentGas = 0
        startingIndex = 0
        for i in range(N):
            currentGas += gas[i]
            if currentGas - cost[i] >= 0:
                currentGas -= cost[i]
                continue
            else:
                # reset status, and start with next stop
                currentGas = 0
                startingIndex = i+1
        
        return startingIndex
            