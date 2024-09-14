#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

#
# Complete the 'droppedRequests' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY requestTime as parameter.
#

'''
Maintain a queque of length 10
Mark violations as -1
Only count drops when pop_left()-ing them - This way we wont count duplicates

pop from Q1 and send to Q2 where we do same check
'''


def droppedRequests(requestTime):
    # print(requestTime)
    if len(requestTime) < 4:
        return 0

    prev = -1
    count = 0
    Q1 = deque()
    Q2 = deque()
    droppedPackets = 0

    for i, time in enumerate(requestTime):
        status = 1
        if time == prev:
            if count > 2:
                status = -1
            else:
                count += 1
        else:
            prev = time
            count = 1

        while Q1 and time - Q1[0][0] >= 10:
            popped10 = Q1.popleft()
            popTime = popped10[0]
            while Q2 and popTime - Q2[0][0] >= 60:
                popped60 = Q2.popleft()
                if popped60[1] == -1:
                    droppedPackets += 1

            if Q2 and not len(Q2) < 60:
                popped10[1] = -1

            Q2.append(popped10)

        if Q1 and not len(Q1) < 20:
            status = -1
        Q1.append([time, status])

    while Q1:
        popped10 = Q1.popleft()
        popTime = popped10[0]
        while Q2 and popTime - Q2[0][0] >= 60:
            popped60 = Q2.popleft()
            if popped60[1] == -1:
                droppedPackets += 1

        if Q2 and not len(Q2) < 60:
            popped10[1] = -1

        Q2.append(popped10)

    while Q2:
        time, status = Q2.popleft()
        if status == -1:
            droppedPackets += 1

    return droppedPackets


if __name__ == '__main__':
    print(droppedRequests([1,1,1,1,2]))
    print(droppedRequests([1, 1, 1, 1, 2, 2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7]))
