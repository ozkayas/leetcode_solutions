class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hMap = dict()
        res = []

        for i,n in enumerate(groupSizes):
            if n not in hMap:
                hMap[n] = [[i]]
            else:
                if len(hMap[n][-1]) < n:
                    hMap[n][-1].append(i)
                else:
                    hMap[n].append([i])
            
        # print(hMap)
        for arr in hMap.values():
            for r in arr:
                res.append(r)

        return res




        