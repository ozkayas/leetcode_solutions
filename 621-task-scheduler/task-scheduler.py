class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        sortedTasks = sorted(freq.items(), key = lambda x:x[1])

    #    print(sortedTasks) 
        char, maxFreq = sortedTasks[-1]

        #how many champions :)
        champs = 0
        for c,f in sortedTasks:
            if f == maxFreq:
                champs += 1


        # A . . A . . A => (freq-1)*n + freq
        maxSizeForMostFreq = (maxFreq -1)*(n+1) + champs

        return max(maxSizeForMostFreq, len(tasks))