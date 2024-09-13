import math


def solution(parcels, extra_parcels):

    # Another way to calculate ceil
    # ceil =  (sum(parcels) + extra_parcels + len(parcels) - 1) // len(parcels)

    ceil = math.ceil( (sum(parcels) + extra_parcels)/len(parcels) )
    return max(max(parcels), ceil)

print(solution([7, 5, 1, 9, 1], 25)) #prints out 10
print(solution([7, 1], 2)) #prints out 10
