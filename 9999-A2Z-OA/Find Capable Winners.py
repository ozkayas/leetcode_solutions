"""Amazon games have recently launched a new multi-player tournament on the platform. Each game of the tournament has 3 rounds. The players are provided with exactly three power boosters at the start of the game and each player is aware of the power boosters of their opponent. In each round, the player can choose to compete with any of the power boosters and any power booster can be used at most once in a particular game. In any particular round, the player with a higher power booster wins.

A player X is considered to be capable of defeating player Y if there exists a rearrangement of power boosters of X such that some rearrangement of power boosters of Y can be defeated in at least 2 out of the three rounds. For example, if power boosters of X = [9, 5, 11] and Y = [7, 12, 3], then

If Y uses the boosters in order [7, 3, 12] then X can use it in order [11, 9, 5] and wins 2 out of the three games as 11 > 3 and 9 > 7. Thus X is capable of defeating Y.
If Y uses the boosters in order [5, 9, 11] then X can use it in order [7, 12, 3] and Y wins 2 out of the three games as 7 > 5 and 12 > 9. Thus Y is also capable of defeating X.
Another example is if X = [2, 3, 1] and Y = [4, 5, 6]. Here X is not capable of defeating Y as Y wins more than Y can not be defeated by X in at least two rounds.

Given the power boosters provided to n players where the three power boosters of the ith player are defined by (power_a[i], power_b[i], power_c[i]), find the number of players who are capable of defeating all other players in a game by using their power boosters optimally. It is guaranteed that all powers of each player's power boosters are distinct.

Function Description

Complete the function findCapableWinners in the editor.

findCapableWinners has the following parameter:

int power_a[n]: the first set of power boosters
int power_b[n]: the second set of power boosters
int power_c[n]: the third set of power boosters
Returns

int: the number of players capable of defeating all other players"""
from typing import List

def solution(a: List[int], b: List[int], c: List[int]) -> int:
    N = len(a)
    players = []
    for i in range(N):
        powers = [a[i], b[i], c[i]]
        players.append(sorted(powers))
    print(players)

    maxA, maxB, maxC = 0 , 0 , 0
    for pA, pB, pC in players:
        maxA = max(maxA, pA)
        maxB = max(maxB, pB)
        maxC = max(maxC, pC)


    # We can also fill these while filling players !!!
    maxPowers = sorted( [maxA, maxB, maxC])

    count = 0
    for playerPowers in players:
        i, j = 0, 0
        while i < 3:
            if playerPowers[i] >= maxPowers[j]:
                i += 1
                j += 1
            else:
                i += 1
        if j >=2:
            count += 1
            print(f"player winning: {playerPowers}")

    return count

power_a = [9, 4, 2]
power_b = [5, 12, 10]
power_c = [11, 3, 13]
print(solution(power_a, power_b, power_c))

power_a = [9, 15, 2, 19]
power_b = [5, 18, 10, 11]
power_c = [11, 3, 13 , 14]
print(solution(power_a, power_b, power_c))
