'''
Minimum Time Spent 🍉
🔥 FULLTIME
Amazon Prime Video has movies in category 'comedy' or 'drama'. Determine the earliest time you can finish at least one movie from each category. The release schedule and duration of the movies are provided.

You can start watching a movie at the time it is release or later.
If you begin a movie at time t, it ends at t + duration.
If a movie ends at time t + duration , the second movie can start at that time, t+ duration, or later.
The movies can be watched in any order.
Complete the function minimumTimeSpent which has the following parameters:

int comedyReleaseTime[n]: release times
int comedyDuration[n]: durations
int dramaReleaseTime[m]: release times
int dramaDuration[m]: durations
Example 1:

Input:  comedyReleaseTime = [1, 4], comedyDuration = [3, 2], dramaReleaseTime = [5, 2], dramaDuration = [2, 2]
Output: 6 
Explanation:

Duration and release time are aligned by index.

Two of the best ways to finish watching one movie from each category at the earliest time are as follows:

- Start watching comedy movie1 at time t = 1 and until t = 1 + 3 = 4. Then, watch the drama movie1 from time t = 4 to t = 4 + 2 = 6.
        
- Start watching a comedy movie2 at time t = 2 and until t = 2 + 2 = 4. Then, watch the drama movie1 from time t = 4 to t = 4 + 2 = 6.

The earliest finish time and also answer is 6.

Examples that are sub-optimal include:

- Start watching a comedy movie2 at time t = 4 and until t = 4 + 2 = 6. Then, watch the drama movie1 from time t = 6 to t = 6 + 2 = 8.

- Start watching a comedy movie1 at time t = 1 and until t = 1 + 3 = 4. Then, watch the drama movie1 from time t = 5 to t = 5 + 2 = 7.
        
Constraints:
1 <= n, m <= 105
1 <= comedyReleaseTime[i], comedyDuration[i], dramaReleaseTime[i], dramaDuration[i] <= 106

'''
def firstFinishTime(releseTimes, durations):
    firstTime = float("inf")
    for i in range(len(releseTimes)):
        thisFinishTime = releseTimes[i] + durations[i]
        firstTime = min(firstTime, thisFinishTime)
    return firstTime

def EarliestPossibleFinish(limit, releaseTimes, durations):
    firstTime = float("inf")
    for i in range(len(releaseTimes)):
        thisFinishTime = max(limit, releaseTimes[i])+ durations[i]
        firstTime = min(firstTime, thisFinishTime)
    return firstTime

def minimumTimeSpent(comedyRT, comedyDur, dramaRT, dramaDur) -> int:
    firstFinishTimeComedy = firstFinishTime(comedyRT, comedyDur)
    firstFinishTimeDrama = firstFinishTime(dramaRT, dramaDur)

    comedyFirstFinish = EarliestPossibleFinish(firstFinishTimeComedy, dramaRT, dramaDur)
    dramaFirstFinish = EarliestPossibleFinish(firstFinishTimeDrama, comedyRT, comedyDur)

    print(comedyFirstFinish, dramaFirstFinish)
    return min(comedyFirstFinish, dramaFirstFinish)

print(minimumTimeSpent([1, 4],[3, 2],[5, 2], [2, 2]))

