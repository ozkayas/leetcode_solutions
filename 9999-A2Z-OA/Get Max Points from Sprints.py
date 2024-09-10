"""
https://www.fastprep.io/problems/get-max-points-from-sprints

Amazon Care is a healthcare and wellbeing portal for its employees.

To promote physical fitness, on the portal they launched a "GetFit" tournament consisting of n sprints. Each sprint lasts for a given number of days and includes several tasks such as push-ups, running, etc. Some tasks are scheduled for each day of the sprint. The ith sprint lasts for days[i] days, and each sprint starts just after the other. That is, if the ithsprint ends on day d, the (i + 1)th sprint starts on day (d + 1). During each sprint, completing the required tasks scheduled on the jth day of the sprint earns the participant j points.

The tournaments are periodic, i.e., as soon as the last sprint of a tournament ends, the first sprint of the next tournament begins. Each tournament, however, has the same schedule of sprints. More formally, the tournament schedule can be considered cyclic in nature and after the last sprint, the first sprint starts again.

An employee decides to participate. However, due to a tight schedule, the employee cannot complete all tasks every day. Instead, the employee will complete the tasks of exactly k consecutive days, hoping to achieve the maximum number of points.

Given the sprint days of n sprints, and the number of days for which the employee competes for k, find the maximum points the employee can score. The training can start and end on any day of any sprint.

Note:

k is guaranteed to be less than the total number of days for which the sprints last.
Also, it is not necessary to start and end the training in the same tournament.
A sprint here denotes a set of activities performed in a particular time period
Example 1:

Input:  days = [2, 3, 2], k = 4
Output: 8
The maximum number of points that can be attained = 2 + 1 + 2 + 3 = 8. One choice is to start on the last day of the first sprint and end on the last day of the second sprint.

"""
from collections import deque


def maxPointsWithKRounds(tournament, K):
    q = deque()  # Use deque for queue operations
    if K == 0:
        return 0

    res = 0
    points = 0

    for tournNo, tournDays in enumerate(tournament+tournament):  # Double the tournament to handle cyclic nature
        print(f"tournNo: {tournNo}, tournDays: {tournDays}")
        for day in range(1, tournDays + 1):
            if len(q) < K:
                points += day
                q.append(day)
            else:
                points -= q.popleft()  # Equivalent to Java's poll()
                points += day
                q.append(day)

            res = max(res, points)

    return res

print(maxPointsWithKRounds([2,3,2], 4)) # 8
print(maxPointsWithKRounds([7, 4, 3, 7, 2], 8)) #32
print(maxPointsWithKRounds([7, 4, 3, 7, 2], 3)) #18
print(maxPointsWithKRounds([2,1,1,4], 5)) #12
