class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        maxAbility = max(worker)

        jobs = [0 for _ in range(maxAbility+1)]

        for i in range(len(difficulty)):
            dif = difficulty[i]
            if dif <= maxAbility:
                jobs[dif] = max(jobs[dif], profit[i])
        
        for i in range(1, len(jobs)):
            jobs[i] = max(jobs[i-1],jobs[i])

        netProfit = 0
        for ability in worker:
            netProfit += jobs[ability]
        
        return netProfit