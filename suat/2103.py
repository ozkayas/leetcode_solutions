class Solution:
    def countPoints(self, rings: str) -> int:
        rodSets = [set() for _ in range(10)]

        p = len(rings)-1

        while p > 0:
            ind = int(rings[p])
            rodSets[ind].add(rings[p-1])
            p -= 2

        count = 0 
        for rodSet in rodSets:
            if len(rodSet) == 3:
                count += 1
        
        return count


"""
set kullanarak deneyelim 
"""