class Solution:
    def maximumSwap(self, num: int) -> int:
        indexTable = [-1 for _ in range(10)]
        numAsList = [int(ch) for ch in str(num)]

        # last seen index of each digit
        # 2736 -> [-1, -1, 0, 2, -1, -1, 3, 1, -1, -1]
        for i, n in enumerate(numAsList):
            indexTable[n] = i

        for i, n in enumerate(numAsList):
            # look for all digits bigger than this, and if exists swap
            for digit in range(9, n, -1):
                if indexTable[digit] > i:
                    numAsList[i], numAsList[indexTable[digit]] = numAsList[indexTable[digit]], numAsList[i]
                    return int("".join([str(num) for num in numAsList]))


        return int("".join([str(num) for num in numAsList]))

        


        