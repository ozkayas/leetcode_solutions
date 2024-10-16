class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        fHeap = []
        for f, ch in zip((a,b,c), "abc"):
            if f: heapq.heappush(fHeap, (-f, ch)) 

        ans = []
        while fHeap:
            f, c = heapq.heappop(fHeap)
            if ans[-2:] == [c, c]:
                if not fHeap: break
                ff, cc = heapq.heappop(fHeap)
                ans.append(cc)
                # add remaining cc if exists still
                if -ff-1 > 0:
                    heapq.heappush(fHeap,(ff+1, cc))
                heapq.heappush(fHeap, (f,c))
            else:
                ans.append(c)
                if -f-1 > 0:
                    heapq.heappush(fHeap,(f+1, c))
        return "".join(ans)
                


        