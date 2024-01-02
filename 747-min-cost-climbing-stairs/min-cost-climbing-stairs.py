class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        N = len(cost)
        memo = {}

        def fn(i:int) -> int:
            if i >= N-2:
                memo[i] = cost[i]
                return memo[i]
            
            if i+2 not in memo:
                memo[i+2] = fn(i+2)
            if i+1 not in memo:
                memo[i+1] = fn(i+1)

            nextStepCost = memo[i+1]
            nextNextStepCost = memo[i+2]

            costOfThis = cost[i] + min(nextStepCost, nextNextStepCost)

            return costOfThis

        return min(fn(0), fn(1))