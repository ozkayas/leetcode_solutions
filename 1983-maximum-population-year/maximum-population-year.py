class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        maxPopulationAndYear = [0, 0]
        curPopulation = 0
        curYear = 0

        bornDates = sorted([log[0] for log in logs])
        dieDates = sorted([log[1] for log in logs])

        b, d = 0, 0

        while b < len(bornDates):
            if bornDates[b] < dieDates[d]:
                curPopulation += 1
                curYear = bornDates[b]
                b += 1
            elif dieDates[d] < bornDates[b]:
                curPopulation -= 1
                d += 1
            else:
                b += 1
                d += 1
            
            if curPopulation > maxPopulationAndYear[0]:
                maxPopulationAndYear[0] = curPopulation
                maxPopulationAndYear[1] = curYear
                print('update data', curPopulation, maxPopulationAndYear)

        return maxPopulationAndYear[1]
            