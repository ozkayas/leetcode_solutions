class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        listCnt = list(counter.items())
        listCnt.sort(key = lambda x:x[1], reverse = True)
        # print(counter)
        # print(listCnt)

        while k > 0:
            key,val = listCnt.pop()
            if val > 1:
                val -= 1
                listCnt.append((key,val))
            k -= 1

            # print(listCnt)

        return len(listCnt)