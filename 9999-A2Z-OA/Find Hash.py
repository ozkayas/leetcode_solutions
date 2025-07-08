
def findHash(param):
    param.sort()

    distinctCount = 0
    targetHash = 0

    for p in param:
        if p > targetHash: 
            distinctCount += 1
            targetHash += 1

    return distinctCount