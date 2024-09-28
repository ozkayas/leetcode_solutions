class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        N = len(segments)
        startingTime = float("inf")
        # curSet = set()
        curSet = 0 ## lets try directly summing, instead of using set

        # {1:[5,8],4:[7]}- {4:[5], 7:[7,9]} 
        # using hashmap to read write O(1) time, 
        #a lternative could be sorting in an array and jumping on these 
        # instead of sweeping all timeline 1 by 1
        starts, ends = defaultdict(list), defaultdict(list)
        for s, e, c in segments:
            starts[s].append(c)
            ends[e].append(c)
            # Saving startTime to start simulation 
            startingTime = min(startingTime, s)
            
        
        ##### --------  SIMULATION -----------
        time, ans = startingTime, []
        lastOperationTime = time

        endCounter = 0 # max value is len(ends), to stop simulation
        while True: ## We will continue until last paint end is handle
            if time in ends:
                if lastOperationTime != time :
                    ans.append([lastOperationTime, time, (curSet)])
                for color in ends[time]:
                    # curSet.remove(color)
                    curSet -= color
                lastOperationTime = time
                endCounter += 1
            if time in starts:
                if lastOperationTime != time and curSet:
                    ans.append([lastOperationTime, time, (curSet)])
                for color in starts[time]:
                    # curSet.add(color)
                    curSet += color
                lastOperationTime = time

            # Check if the simulation ended, last painting ended
            if endCounter >= len(ends):
                break
            time += 1
        return ans
            

