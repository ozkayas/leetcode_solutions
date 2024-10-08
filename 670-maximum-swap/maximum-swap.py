class Solution:
    def maximumSwap(self, num: int) -> int:
        # To ease swap and early return
        numAsList = [int(ch) for ch in str(num)]
        indexTable = defaultdict(list)

        def intParse(l:list[int]) -> int:
            return int("".join([str(n) for n in l]))


        # Filling indexes from back, for easier popping when an element is used
        for i in range(len(numAsList)-1, -1, -1):
            indexTable[numAsList[i]].append(i)

        for i, n in enumerate(numAsList):
            # does table has a bigger key than this at a later index?
            for x in range(9, n, -1):
                if x in indexTable and indexTable[x][0] > i:
                    #swap and return
                    numAsList[i], numAsList[indexTable[x][0]] = numAsList[indexTable[x][0]], numAsList[i] 
                    return intParse(numAsList)
            # can not swap so remove this from the table, because it is used now
            indexTable[n].pop()
            if not indexTable[n]: del indexTable[n]

        return intParse(numAsList)

        