class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waitingTimes = []
        curTime = customers[0][0]
        
        for enter, during in customers:
            endTimeOfCurCust = max(enter, curTime) + during
            waitingTime = endTimeOfCurCust - enter
            waitingTimes.append(waitingTime)
            curTime = endTimeOfCurCust
        
        return sum(waitingTimes)/len(waitingTimes)



        