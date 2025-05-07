class Solution:
    def romanToInt(self, s: str) -> int:
        table = {"I":1,
                    "V":5,
                    "X":10,
                    "L":50,
                    "C":100,
                    "D":500,
                    "M":1000}

        lastAdded = 0
        total = 0
        for roman in s:
            if lastAdded == 0:
                total += table[roman]
                lastAdded = table[roman]
            else:
                if table[roman] <= lastAdded:
                    total += table[roman]
                    lastAdded = table[roman]
                else:
                    total -= lastAdded*2
                    total += table[roman]
                    lastAdded = table[roman]
        return total


        