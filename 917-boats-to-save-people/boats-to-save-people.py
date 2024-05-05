class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        l, r = 0, len(people)-1

        while l <= r:
            curBoat = []

            # add people since there is enough space on the boat
            while len(curBoat)<2 and people[r] <= (limit - sum(curBoat)):
                curBoat.append( people[r])
                # if curBoat == limit:
                r -= 1
        
            while len(curBoat)<2 and people[l] <= (limit - sum(curBoat)):
                curBoat.append(people[l])
                # if curBoat == limit:
                l += 1               
        
            boats += 1
        return boats
                


'''
limit = 6
curBoat = 6
boats: 1
[2 2 2 3 3]
 lr



'''
        